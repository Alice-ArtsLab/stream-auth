'''
User model
'''
import random
import string
import logging
import bcrypt

STREAM_KEY_LENGTH = 64


def generate_stream_key(key_length: int):
    '''
    Generate a new stream key
    '''
    key_types = string.ascii_letters + string.digits
    return ''.join(random.choice(key_types) for i in range(key_length))


class User:
    '''
    User class, for managing a specific user
    '''

    def __init__(self, username: str, password: str):
        salt = bcrypt.gensalt()
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.stream_key = generate_stream_key(STREAM_KEY_LENGTH)

    def regenerate_stream_key(self):
        '''
        Recreate stream_key
        '''
        self.stream_key = generate_stream_key(STREAM_KEY_LENGTH)

    def check_passwrod(self, password: str):
        input_pass = password.encode('utf-8')
        result = bcrypt.checkpw(input_pass, self.password)
        return result

    def change_password(self, current_password: str, new_password: str):
        '''
        Changes user defualt password
        '''
        ecpass = current_password.encode('utf-8')
        enpass = new_password.encode('utf-8')
        result = bcrypt.checkpw(ecpass, self.password)
        if not result:
            logging.warning("PASSWORDS DO NOT MATCH")

        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(enpass, salt)
