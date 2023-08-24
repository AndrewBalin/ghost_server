from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode='threading', transports=['websocket'])

messages = []

@socketio.on('send_message')
def send_message(data):
    print(data)
    messages.append(f'[{data["nickname"]}]: {data["message"]}')
    emit('get_message', data)

@app.route('/')
def show_messages():
    msg = '</br>'.join(messages)
    return msg

socketio.run(app, allow_unsafe_werkzeug=True)