from fastapi import FastAPI, Depends, Security
from fastapi.middleware.cors import CORSMiddleware
from .auth import verify_token
from .schemas import UserProfile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Default Vite port
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/whoami", response_model = UserProfile)
def who_am_i(payload: dict = Security(verify_token)):
    user_name = payload.get("name") or payload.get("nickname") or "Authorzed User"
    user_id = payload.get("sub", "Unknown ID")

    return {
        "name" : user_name,
        "user_id": user_id
    }