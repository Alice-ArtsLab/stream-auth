'''
For managing users
'''

from tinydb import TinyDB, Query
from stream_auth.models.user import User
from stream_auth import settings

db = TinyDB(settings.USER_DATABASE)
query = Query()


def create_user(username: str, hash_pass: str):
    '''
    Creates a new unique user, with a unique stream_key
    '''

    if len(db.search(query.username == username)) != 0:
        raise ValueError("Username already exists.")

    user = User(username, hash_pass)
    while db.search(query.stream_key == user.stream_key):
        user.regenerate_stream_key()

    db.insert(user.__dict__)
    return user


def search_stream_key(stream_key: str):
    '''
    Search for a specific stream key
    '''
    return db.search(query.stream_key == stream_key)
