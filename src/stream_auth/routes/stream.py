'''
For controlling streams
'''

# import logging
from flask import Blueprint, Response, request, redirect
from stream_auth.middlewares.auth import auth
from stream_auth.middlewares import jwt
from stream_auth.models.stream import Stream as StreamModel
from stream_auth.database import user

stream = Blueprint('user', __name__)


@stream.route('/create_stream', methods=['POST'])
@auth
def create_stream():
    json = request.get_json()
    username = json['username']
    title = json['name']
    description = json['description']
    StreamModel(username, title, description)


@stream.route('/publish_check')
def publish_check():

    # TODO: check if user created stream

    # check if already redirected
    token = request.form.get('token')
    if jwt.verify(token):
        return Response('OK', 200)

    # get user
    try:
        stream_key = request.form.get('name')
        stream_user = user.search_stream_key(stream_key)[0]['username']
        username = stream_user['username']

    except IndexError:
        return Response('Invalid Stream Key', 401)

    token = jwt.create_token(username, stream_key, 10)
    return redirect(f'rtmp://127.0.0.1:33000/live/{username}?{token}', code=302)
