from datetime import timedelta, datetime, timezone
from typing import Optional
from jose import jwt, JWTError
from schemas import token_creation

SECRET_KEY = "7AlBaQQSuVfxYVeLyKX1G-4WfVc2PTdxE7BYQIUeSOYmxmRXpo4AqbfkFLLsjR7TZA_7p9Fu38raedB2pH31Og"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expire_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.now(timezone.utc) + expire_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return token_creation.TokenData(username= username)
    except JWTError:
        raise credentials_exception


