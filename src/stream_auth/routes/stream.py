'''
For controlling streams
'''

# import logging
from flask import Blueprint, Response, request
from stream_auth.middlewares.auth import auth
from stream_auth.models.stream import Stream as StreamModel

stream = Blueprint('user', __name__)


@stream.route('/create_stream', methods=['POST'])
@auth
def create_stream():
    json = request.get_json()
    username = json['username']
    title = json['name']
    description = json['description']
    # stream_key = json['stream_key']
    StreamModel(title, description, username)
