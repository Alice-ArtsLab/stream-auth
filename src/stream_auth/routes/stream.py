'''
For controlling streams
'''

# import logging
from flask import Blueprint, Response, request, redirect
from stream_auth.middlewares.auth import auth
from stream_auth.middlewares import jwt
from stream_auth.models.stream import Stream as StreamModel
from stream_auth.database import user

stream = Blueprint('stream', __name__)


@stream.route('/create_stream', methods=['POST'])
@auth
def create_stream():
    json = request.get_json()
    username = json['username']
    title = json['name']
    description = json['description']
    StreamModel(username, title, description)


@stream.route('/publish_check', methods=['POST'])
def publish_check():

    # TODO: check if user created stream

    # get user
    stream_key = request.form.get('stream_key')
    username = request.form.get('name')
    print(username, stream_key)
    try:
        stream_user = user.search_user(username)[0]

        if username != stream_user['username'] or not jwt.verify_stream_key(stream_key):
            raise ValueError('Invalid Token')

    except (IndexError, ValueError):
        return Response('Invalid Stream Key', 401)

    return Response('OK', 200)


@stream.route('/test')
def test():

    stream_key = request.args.get('stream_key')
    if jwt.verify_token(stream_key):
        return Response('OK', 200)

    return Response('Invalid Stream Key', 401)

    # jwt.verify(stream_key)
