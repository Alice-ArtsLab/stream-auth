import time
import jwt
from stream_auth import settings


def read_key(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


JWT_PRIV_KEY = read_key(settings.JWT_PRIV_PATH)
JWT_PUB_KEY = read_key(settings.JWT_PUB_PATH)


def create_stream_key(username: str):
    payload = {'username': username}
    return jwt.encode(payload, JWT_PRIV_KEY, algorithm="RS256")


def create_token(username: str, stream_key: str, exp: int = settings.JWT_EXP_TIME):
    exp = time.time() + exp
    payload = {'username': username, 'stream_key': stream_key, 'exp': exp}
    return jwt.encode(payload, JWT_PRIV_KEY, algorithm="RS256")


def verify(token: str):
    jwt.decode(token, JWT_PUB_KEY, algorithms=["RS256"])
    # try:
        # jwt.decode(token, JWT_PUB_KEY, algorithms=["RS256"])
    # except (jwt.exceptions.ExpiredSignatureError, jwt.InvalidTokenError):
        # return False

    return True


def decode_token(token: str):
    return jwt.decode(token, JWT_PUB_KEY, algorithms=["RS256"])
