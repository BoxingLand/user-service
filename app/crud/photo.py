from uuid import uuid4, UUID

from loguru import logger

from app.database.connection import pool
from app.user import user_pb2


async def add_photo_to_user(
        photo_data: user_pb2.UploadFileRequest,
        photo_name: str
):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    INSERT INTO "photo" (id, user_id, photo_name, is_avatar, updated_at, created_at, is_deleted )
                    VALUES('{uuid4()}',
                            '{photo_data.user_id}',
                            '{photo_name}',
                            '{photo_data.is_avatar}',
                            now()::timestamp,
                            now()::timestamp,
                            FALSE
                    );
                                """)
                await conn.commit()

    except Exception as e:
        logger.error(e)
        await conn.rollback()

async def update_avatar(
    user_id: UUID
):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    UPDATE "photo"
                    SET is_avatar = FALSE,
                    updated_at = now()::timestamp
                    WHERE user_id = '{user_id}';
                                """)
                await conn.commit()

    except Exception as e:
        logger.error(e)
        await conn.rollback()

