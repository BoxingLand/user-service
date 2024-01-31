from uuid import UUID, uuid4

from loguru import logger
from psycopg.rows import class_row

from app.database.connection import pool
from app.exceptions.user_errors import UserCreateException, UserEmailNotFoundException
from app.models.user import User, BoxerProfile
from app.user import user_pb2


async def create_user(
        signup_data: user_pb2.SignupRequest,
) -> None:
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    WITH user_data AS (
                        INSERT INTO "user" (id, email, phone_number, password, updated_at, created_at, is_active, is_deleted)
                        VALUES ('{uuid4()}',
                                '{signup_data.email.lower()}',
                                '{signup_data.phone_number}',
                                '{signup_data.password}',
                                now()::timestamp,
                                now()::timestamp,
                                FALSE,
                                FALSE
                        )
                        RETURNING id
                    )
                    INSERT INTO "{signup_data.account_type}" (id, user_id, updated_at, created_at, is_deleted)
                    VALUES('{uuid4()}',
                            (SELECT id FROM user_data),
                            now()::timestamp,
                            now()::timestamp,
                            FALSE
                    );
                                """)
                await conn.commit()
    except Exception as e:
        logger.error(e)
        await conn.rollback()
        raise UserCreateException()  # noqa: B904


async def get_user_by_id(
        user_id: UUID
) -> User | None:
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(User)) as cur:
            await cur.execute(f"""
                   SELECT *
                   FROM "user"
                   WHERE id = '{user_id}' AND is_deleted = FALSE;
                               """)
            user = await cur.fetchone()
            return user


async def get_user_by_email(
        email: str,
) -> User | None:
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(User)) as cur:
            await cur.execute(f"""
                   SELECT *
                   FROM "user"
                   WHERE email = '{email}' AND is_deleted = FALSE;
                               """)
            user = await cur.fetchone()
            return user


async def get_user_by_phone_number(
        phone_number: str,
) -> User | None:
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(User)) as cur:
            await cur.execute(f"""
                   SELECT *
                   FROM "user"
                   WHERE phone_number = '{phone_number}' AND is_deleted = FALSE;
                               """)
            user = await cur.fetchone()
            return user


async def user_email_exists(
        email: str,
) -> str | None:
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT email
                FROM "user"
                WHERE email = '{email}' AND is_deleted = FALSE;
                            """)
            user_email = await cur.fetchone()
            if user_email is None:
                return None
            return user_email[0]


async def user_phone_number_exists(
        phone_number: str,
) -> str | None:
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT phone_number
                FROM "user"
                WHERE phone_number = '{phone_number}' AND is_deleted = FALSE;
                            """)
            user_phone_number = await cur.fetchone()
            if user_phone_number is None:
                return None
            return user_phone_number[0]


async def get_verify_token_by_user_email(
        user_email: str,
):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT verify_token
                FROM "user"
                WHERE email = '{user_email}' AND is_deleted = FALSE;
                            """)
            user_verify_token = await cur.fetchone()
            return user_verify_token[0]


async def set_verify_token(
        email: str,
        verify_token: str
):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    UPDATE "user"
                    SET verify_token = '{verify_token}',
                    updated_at = now()::timestamp
                    WHERE email = '{email}' AND is_deleted = FALSE;
                                """)
                await conn.commit()

    except Exception as e:
        logger.error(e)
        await conn.rollback()
        raise UserEmailNotFoundException(email=email)  # noqa: B904


async def verify_user(
        user_email: str,
) -> None:
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    UPDATE "user"
                    SET is_active = True,
                    updated_at = now()::timestamp
                    WHERE email = '{user_email}' AND is_deleted = FALSE;
                                """)
                await conn.commit()

    except Exception as e:
        logger.error(e)
        await conn.rollback()


async def update_user_by_id(
        update_data: user_pb2.UpdateUserProfileRequest,
) -> None:
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    UPDATE "user"
                    SET first_name = COALESCE(
                        {f"'{update_data.first_name}'" if update_data.first_name != '' else 'NULL'},
                        first_name
                    ),
                    last_name = COALESCE(
                        {f"'{update_data.last_name}'" if update_data.last_name != '' else 'NULL'},
                        last_name
                    ),
                    middle_name = COALESCE(
                        {f"'{update_data.middle_name}'" if update_data.middle_name != '' else 'NULL'},
                        middle_name
                    ),
                    sex = COALESCE(
                        {f"'{update_data.sex}'" if update_data.sex != '' else 'NULL'},
                        sex
                    ),
                    birthday = COALESCE(
                        {f"'{update_data.birthday}'" if update_data.birthday != '' else 'NULL'},
                        birthday
                    ),
                    country = COALESCE(
                        {f"'{update_data.country}'" if update_data.country != '' else 'NULL'},
                        country
                    ),
                    region = COALESCE(
                        {f"'{update_data.region}'" if update_data.region != '' else 'NULL'},
                        region
                    ),
                    city = COALESCE(
                        {f"'{update_data.city}'" if update_data.city != '' else 'NULL'},
                        city
                    ),
                    updated_at = now()::timestamp
                    WHERE id = '{update_data.user_id}' AND is_deleted = FALSE;
                                """)
            await conn.commit()
    except Exception as e:
        logger.error(e)
        await conn.rollback()


async def update_user_password(
        user_id: UUID,
        new_password: str,
) -> None:
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    UPDATE "user"
                    SET password = '{new_password}',
                    updated_at = now()::timestamp
                    WHERE id = '{user_id}' AND is_deleted = FALSE;
                                """)
                await conn.commit()

    except Exception as e:
        logger.error(e)
        await conn.rollback()


async def is_user_role_exist(
        user_id: UUID,
        role: str,
):
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"""
                SELECT id
                FROM "{role}"
                WHERE user_id = '{user_id}' AND is_deleted = FALSE;
                            """)
            data = await cur.fetchone()
            if data is None:
                return None
            return data[0]


async def add_role_to_user(
        role_data: user_pb2.AddRoleRequest,
):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    INSERT INTO "{role_data.account_type}" (id, user_id, updated_at, created_at, is_deleted)
                    VALUES('{uuid4()}',
                            '{role_data.user_id}',
                            now()::timestamp,
                            now()::timestamp,
                            FALSE
                    );
                                """)
                await conn.commit()

    except Exception as e:
        logger.error(e)
        await conn.rollback()


async def delete_user(
        user_id: UUID,
):
    try:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f"""
                    UPDATE "user"
                    SET is_deleted = TRUE,
                    updated_at = now()::timestamp
                    WHERE id = '{user_id}';

                    UPDATE "boxer"
                    SET is_deleted = TRUE,
                    updated_at = now()::timestamp
                    WHERE id = '{user_id}';

                    UPDATE "coach"
                    SET is_deleted = TRUE,
                    updated_at = now()::timestamp
                    WHERE id = '{user_id}';

                    UPDATE "judge"
                    SET is_deleted = TRUE,
                    updated_at = now()::timestamp
                    WHERE id = '{user_id}';

                    UPDATE "organizer"
                    SET is_deleted = TRUE,
                    updated_at = now()::timestamp
                    WHERE id = '{user_id}';
                                """)
                await conn.commit()

    except Exception as e:
        logger.error(e)
        await conn.rollback()


async def boxer_profile_by_id(
        user_id: UUID,
) -> BoxerProfile | None:
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(BoxerProfile)) as cur:
            await cur.execute(f"""
                SELECT u.first_name, u.last_name, u.sex, u.birthday, u.country, u.region, b.weight, b.height, b.athletic_distinction, p.photo_name
                FROM "user" u
                JOIN "boxer" b ON u.id = b.user_id
                LEFT JOIN "photo" p ON u.id = p.user_id AND p.is_avatar = TRUE
                WHERE u.id = '{user_id}' AND b.is_deleted = FALSE;
                            """)
            data = await cur.fetchone()
            if data is None:
                return None
            return data