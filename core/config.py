from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEV_DATABASE_URL: str
    TEST_DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()