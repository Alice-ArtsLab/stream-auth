'''
For controlling user routes
'''

import logging
from flask import Blueprint, Response, request, jsonify, make_response
from stream_auth.models.user import User
from stream_auth.database import user as userdb
from stream_auth.middlewares import jwt

user = Blueprint('user', __name__)


@user.route('/signin', methods=['POST'])
def create():
    '''
    Create a new user
    '''

    json = request.get_json()
    username = json['username']
    password = json['password']

    new_user = userdb.create_user(username, password)

    logging.info('User %s created with stream key %s',
                 new_user.username, new_user.stream_key)

    return Response('OK', 200)


@user.route('/login', methods=['POST'])
def login():
    '''
    User log in
    '''

    json = request.get_json()
    username = json['username']
    password = json['password']

    try:
        log_user = userdb.search_user(username)[0]
    except IndexError:
        return Response('User or password incorrect', 401)

    if not log_user.check_password(password):
        return Response('User or password incorrect', 401)

    token = jwt.create_token(log_user.username, log_user.stream_key)
    logging.info('User %s logged in', log_user.username)

    return make_response(jsonify({'token': token}), 201)


@user.route('/logout', methods=['POST'])
def logout():
    '''
    Create a new user
    '''

    json = request.get_json()
    username = json['username']
    password = json['password']

    new_user = User(username, password)

    logging.info('User %s logged out', new_user.username)

    return Response('OK', 200)
