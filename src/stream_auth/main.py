'''
Entry point
'''

import logging
from flask import Flask, render_template
from flask_sock import Sock

from stream_auth import settings
from src.stream_auth.controller import AuthController

# from stream_auth.routes.user import user as user_routes
# from stream_auth.routes.stream import stream as stream_routes


app = Flask(__name__)
sock = Sock(app)
logging.basicConfig(level=logging.INFO)
clientes = set()

@app.route('/')
def index():
    return render_template('index.html')
    # return "<p>Tudo funcionando corretamente</p>"

@sock.route('/chat')
def echo(ws):
    # Add the websocket to a list of connected clients
    clientes.add(ws)


    try: 
        while True:
            # Receive a message from the client
            logging.warn(ws)  # will not print anything
            message = ws.receive()

            logging.info(message);
            # Broadcast the message to all connected clients
            for client in clientes:
                client.send(message)
    finally:
        clientes.remove(ws)

    
@sock.route('/signin')
def echo(ws):
    AuthController.principal(ws);

# def main(*args, **kwargs):
# app.register_blueprint(user_routes)
# app.register_blueprint(stream_routes)


if __name__ == "__main__":
    print(settings.PORT)
    app.run(host=settings.HOST, port=33003)

