from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    DATABASE_USER: str = "admin"
    DATABASE_PASSWORD: str = "admin"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int | str = "2346"
    DATABASE_NAME: str = "user"

    MINIO_ROOT_USER: str = "admin"
    MINIO_ROOT_PASSWORD: str = "adminadmin"
    MINIO_URL: str = "localhost:9000"
    MINIO_BUCKET: str = "boxing-land"

    DB_POOL_SIZE: int = 90

    SERVER_PORT: int = 50051
    class Config:
        case_sensitive = True
        validate_assignment = True
