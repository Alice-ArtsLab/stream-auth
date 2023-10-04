'''
Entry point
'''

import logging
from flask import Flask
from stream_auth import settings
from stream_auth.routes.user import user as user_routes
from stream_auth.routes.stream import user as stream_routes


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    app.register_blueprint(user_routes)
    app.register_blueprint(stream_routes)

    app.run(host=settings.HOST, port=settings.PORT)


if __name__ == "__main__":
    main()
