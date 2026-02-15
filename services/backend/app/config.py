from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):

    AUTH0_DOMAIN: str
    AUTH0_AUDIENCE: str
    AUTH0_ALGORITHM :str
    
    API_TITLE: str = "WhoAmI"

    
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:8001",
        "http://localhost:5173",
        "https://whoami-frontend-ochre.vercel.app/", #frontend
        "https://whoami-five-theta.vercel.app/", #backend

    ]

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()