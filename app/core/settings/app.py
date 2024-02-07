from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int | str | None = None
    DATABASE_NAME: str

    AUTH_SERVICE_URL: str

    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_URL: str
    MINIO_BUCKET: str

    DB_POOL_SIZE: int

    SERVER_PORT: int
    METRICS_PORT: int

    def get_db_connection_scheme(self):
        if self.DATABASE_PORT is not None:
            return f"""
                dbname={self.DATABASE_NAME}
                user={self.DATABASE_USER}
                password={self.DATABASE_PASSWORD}
                host={self.DATABASE_HOST}
                port={self.DATABASE_PORT}
                """
        else:
            return f"""
                dbname={self.DATABASE_NAME}
                user={self.DATABASE_USER}
                password={self.DATABASE_PASSWORD}
                host={self.DATABASE_HOST}
                """

    class Config:
        case_sensitive = True
        validate_assignment = True
