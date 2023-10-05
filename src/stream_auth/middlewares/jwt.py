import time
import jwt as jwtlib
from stream_auth import settings


def read_key(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


JWT_PRIV_KEY = read_key(settings.JWT_PRIV_PATH)
JWT_PUB_KEY = read_key(settings.JWT_PUB_PATH)
STREAM_KEY_PRIV_KEY = read_key(settings.STREAM_KEY_PRIV_PATH)
STREAM_KEY_PUB_KEY = read_key(settings.STREAM_KEY_PRIV_PATH)


def create_stream_key(username: str):
    payload = {'username': username}
    return jwtlib.encode(payload, STREAM_KEY_PRIV_KEY, algorithm="ES256")


def verify_stream_key(stream_key: str):
    try:
        jwtlib.decode(stream_key, STREAM_KEY_PUB_KEY, algorithms=["ES256"])
    except (jwtlib.exceptions.ExpiredSignatureError, jwtlib.InvalidTokenError):
        return False

    return True


def decode_stream_key(stream_key: str):
    return jwtlib.decode(stream_key, STREAM_KEY_PUB_KEY, algorithms=["RS256"])


def create_token(username: str, stream_key: str, exp: int = settings.JWT_EXP_TIME):
    exp = time.time() + exp
    payload = {'username': username, 'stream_key': stream_key, 'exp': exp}
    return jwtlib.encode(payload, JWT_PRIV_KEY, algorithm="RS256")


def verify_token(token: str):
    # return jwtlib.decode(token, JWT_PUB_KEY, algorithms=["RS256"])
    try:
        jwtlib.decode(token, JWT_PUB_KEY, algorithms=["RS256"])
    except (jwtlib.exceptions.ExpiredSignatureError, jwtlib.InvalidTokenError):
        return False

    return True


def decode_token(token: str):
    return jwtlib.decode(token, JWT_PUB_KEY, algorithms=["RS256"])
