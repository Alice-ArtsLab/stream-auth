'''
Entry point
'''

import logging
from flask import Flask
from stream_auth import settings
from stream_auth.routes.user import user as user_routes


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    app.register_blueprint(user_routes)
    app.run(host=settings.HOST, port=settings.PORT)


if __name__ == "__main__":
    main()
