Note : This page is created by AI

# WhoAmI

Secure "Who Am I" authentication app using Auth0, FastAPI, and React. Users log in via Auth0, and the app reveals their authenticated identity by calling a protected backend API that verifies JWT tokens.

## Tech Stack

- **Backend:** FastAPI, PyJWT, Auth0
- **Frontend:** React 18, Vite, @auth0/auth0-react
- **Auth:** Auth0 (OAuth2 / OpenID Connect, RS256 JWT)

## Project Structure

```
services/
├── backend/
│   └── app/
│       ├── main.py          # FastAPI app with /whoami endpoint
│       ├── auth.py          # JWT token verification via JWKS
│       ├── config.py        # Pydantic settings (env vars)
│       └── schemas.py       # UserProfile model
└── frontend/
    └── src/
        ├── main.jsx         # Entry point with Auth0Provider
        ├── App.jsx          # Main app component
        └── components/
            ├── LoginButton.jsx
            ├── LogoutButton.jsx
            └── ProfileDisplay.jsx
```

## Auth Flow

1. User clicks **Log In** and is redirected to Auth0
2. After login, the frontend silently acquires an access token
3. Frontend calls `GET /whoami` with the token in the `Authorization` header
4. Backend verifies the JWT signature, expiry, audience, and issuer using Auth0's JWKS endpoint
5. Backend fetches user info from Auth0 and returns `{ name, user_id }`

## Prerequisites

- Python 3.10+
- Node.js 18+
- An [Auth0](https://auth0.com) tenant with:
  - A **Single Page Application** (for the frontend)
  - An **API** (for the backend audience)

## Setup

### 1. Clone and configure environment variables

```bash
# Backend
cp services/backend/.env.example services/backend/.env
# Fill in AUTH0_DOMAIN and AUTH0_AUDIENCE

# Frontend
cp services/frontend/.env.example services/frontend/.env
# Fill in VITE_AUTH0_DOMAIN, VITE_AUTH0_CLIENT_ID, and VITE_AUTH0_AUDIENCE
```

### 2. Start the backend

```bash
pip install -r requirements.txt
uvicorn services.backend.app.main:app --port 8001 --reload
```

### 3. Start the frontend

```bash
cd services/frontend
npm install
npm run dev
```

The frontend runs on `http://localhost:5173` and the backend on `http://localhost:8001`.

## API

| Method | Endpoint  | Auth     | Response                        |
|--------|-----------|----------|---------------------------------|
| GET    | `/whoami` | Bearer JWT | `{ "name": "...", "user_id": "..." }` |

## Environment Variables

### Backend (`services/backend/.env`)

| Variable          | Description                     |
|-------------------|---------------------------------|
| `AUTH0_DOMAIN`    | Auth0 tenant domain             |
| `AUTH0_AUDIENCE`  | API identifier from Auth0       |
| `AUTH0_ALGORITHM` | Signing algorithm (default RS256) |

### Frontend (`services/frontend/.env`)

| Variable              | Description                  |
|-----------------------|------------------------------|
| `VITE_AUTH0_DOMAIN`   | Auth0 tenant domain          |
| `VITE_AUTH0_CLIENT_ID`| Auth0 SPA client ID          |
| `VITE_AUTH0_AUDIENCE` | API identifier from Auth0    |
