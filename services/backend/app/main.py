from fastapi import FastAPI, Depends, Security, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
from .auth import verify_token
from .config import settings
from .schemas import UserProfile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/whoami", response_model = UserProfile)
def who_am_i(request: Request, payload: dict = Security(verify_token)):
    print(payload)
    user_id = payload.get("sub", "Unknown ID")


    # Access token for custom APIs doesn't include profile claims.
    # Fetch the user's name from Auth0's /userinfo endpoint.
    token = request.headers.get("Authorization", "").removeprefix("Bearer ")
    userinfo_url = f"https://{settings.AUTH0_DOMAIN}/userinfo"
    resp = requests.get(userinfo_url, headers={"Authorization": f"Bearer {token}"})

    if resp.ok:
        userinfo = resp.json()
        user_name = userinfo.get("name") or userinfo.get("nickname") or "Authorized User"
    else:
        user_name = payload.get("name") or payload.get("nickname") or "Authorized User"

    return {
        "name" : user_name,
        "user_id": user_id
    }