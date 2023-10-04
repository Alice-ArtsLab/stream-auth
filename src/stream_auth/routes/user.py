'''
For controlling user routes
'''

import logging
from flask import Blueprint, Response, request
from stream_auth.models.user import User

user = Blueprint('user', __name__)


@user.route("/signin", methods=["POST"])
def create():
    '''
    Create a new user
    '''

    json = request.get_json()
    username = json['username']
    password = json['password']

    new_user = User(username, password)

    logging.info('User %s created with stream key %s',
                 new_user.username, new_user.stream_key)

    return Response('OK', 200)


@user.route("/login", methods=["POST"])
def login():
    '''
    Create a new user
    '''

    json = request.get_json()
    username = json['username']
    password = json['password']

    # TODO: actully do this
    new_user = User(username, password)

    # logging.info('User %s created with stream key %s',
                 # new_user.username, new_user.stream_key)

    return Response('OK', 200)


@user.route("/logout", methods=["POST"])
def logout():
    '''
    Create a new user
    '''

    json = request.get_json()
    username = json['username']
    password = json['password']

    # TODO: actully do this
    new_user = User(username, password)

    # logging.info('User %s created with stream key %s',
                 # new_user.username, new_user.stream_key)

    return Response('OK', 200)
