'''
Middleware for checking if access is authorized
'''

from functools import wraps
from flask import request, abort
from stream_auth.middlewares import jwt


def auth(route_func):
    '''
    Decorator to verify JWT in http header
    '''
    @wraps(route_func)
    def wrapper(*args, **kwargs):

        token = request.headers.get('Token')
        if token is None or jwt.verify(token):
            abort(401)

        return route_func(*args, **kwargs)

    return wrapper
