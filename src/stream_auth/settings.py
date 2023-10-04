'''
Settings file, where all globals should be
'''
import os

HOST = '0.0.0.0'
PORT = 8080

APP_DIR = os.path.dirname(os.path.realpath(__file__))
KEY_DIR = os.path.join(APP_DIR, 'keys')

JWT_PRIV_PATH = os.path.join(KEY_DIR, 'jwtRS256.key')
JWT_PUB_PATH = os.path.join(KEY_DIR, 'jwtRS256.key.pub')
JWT_EXP_TIME = 2592000

USER_DATABASE = '/home/gabriel/db.json'
STREAM_KEY_LENGTH = 32
