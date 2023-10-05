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
    try:
        stream_key = request.form.get('stream_key')
        username = request.form.get('name')
        stream_user = user.search_user(username)[0]
        if username != stream_user['username']:
            raise ValueError

    except (IndexError):
        print('vish')
        return Response('Invalid Stream Key', 401)

    jwt.verify(stream_key.encode('utf-8'))
    return Response('OK', 200)
