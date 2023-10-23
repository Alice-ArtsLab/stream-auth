'''
Settings file, where all globals should be
'''
import os

HOST = '0.0.0.0'
# PORT = 33002

APP_DIR = os.path.dirname(os.path.realpath(__file__))
KEY_DIR = os.path.join(APP_DIR, 'keys')

JWT_PRIV_PATH = os.path.join(KEY_DIR, 'jwtRS256.key')
JWT_PUB_PATH = os.path.join(KEY_DIR, 'jwtRS256.key.pub')
STREAM_KEY_PRIV_PATH = os.path.join(KEY_DIR, 'streamkeyEC256.key')
STREAM_KEY_PUB_PATH = os.path.join(KEY_DIR, 'streamkeyEC256.key.pub')
JWT_EXP_TIME = 2592000

DBS_PATH = os.path.join(APP_DIR, 'dbs')
USER_DATABASE = os.path.join(DBS_PATH, 'users.json')
STREAM_DATABASE = os.path.join(DBS_PATH, 'streams.json')
LIVE_STREAM_DATABASE = os.path.join(DBS_PATH, 'live_streams.json')

STREAM_KEY_LENGTH = 32
