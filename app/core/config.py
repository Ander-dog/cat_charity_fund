from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    app_description: str = 'Благотворительный фонд поддержки котиков'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = 'superuser@mail.com'
    first_superuser_password: Optional[str] = 'password'

    class Config:
        env_file = '.env'


settings = Settings()
