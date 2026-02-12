from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):

    AUTH0_DOMAIN: str
    API_AUDIENCE: str
    ALGORITHMS: List[str] = ["RS256"]
    
    API_TITLE: str = "WhoAmI API"
    
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://*.vercel.app"
    ]

    class Config:
        env_file = ".env"

settings = Settings()