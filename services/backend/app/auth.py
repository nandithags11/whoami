from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import PyJWKClient, decode, exceptions
from .config import settings

security =HTTPBearer()

#auth0 configuration from settings
JWKS_URL = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"
ISSUER = f"https://{settings.AUTH0_DOMAIN}/"
jwks_client = PyJWKClient(JWKS_URL)

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        #fetch jws public key
        signing_key = jwks_client.get_signing_key_from_jwt(token).key

        #decode and validate the token
        payload = decode(
            token,
            signing_key,
            algorithms=settings.ALGORITHMS,
            audience=settings.API_AUDIENCE,
            issuer=ISSUER,
        )

        return payload
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code = 401, detail = "Token has expired")
    except exceptions.InvalidTokenError as e:
        raise HTTPException(status_code =401, detail = f"Invalid token: {str(e)}")
    except Exception:
        raise HTTPException(status_code =401, detail = "Token authentication failed")

