from datetime import datetime, timedelta, timezone

from jwt import encode 

SECRET_KEY = "secret-key-api-app"
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    encode_token = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    encode_token.update({'expire': expire.timestamp()})
    jwt_encoded = encode(encode_token, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_encoded