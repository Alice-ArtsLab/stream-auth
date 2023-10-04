'''
For managing streams
'''

from tinydb import TinyDB, Query
from stream_auth.models.stream import Stream as StreamModel
from stream_auth import settings

live_db = TinyDB(settings.LIVE_STREAM_DATABASE)
stream_db = TinyDB(settings.STREAM_DATABASE)
query = Query()


def create_stream(username: str, title: str, description: str):
    '''
    Creates a new stream for a user
    '''

    if len(live_db.search(query.username == username)) > 0:
        raise ValueError('User already live')

    stream = StreamModel(username, title, description)

    live_db.insert(stream.__dict__)
    return stream


def search_live_stream(username: str):
    return live_db.search(query.username == username)


def stop_stream(username: str):
    '''
    Search for a live stream
    '''

    stream = search_live_stream(username)

    live_db.remove(query.username == username)
    stream_db.insert(dict(stream[0]))
    return stream
