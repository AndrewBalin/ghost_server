import socketio

sio = socketio.Client()

@sio.on('message')
def on_message(data):
    print('I received a message!')

sio.connect('http://127.0.0.1:5000')

login = input("Введите логин: ")
while True:
    message = input("Введите сообщение: ")
    sio.emit({'login': login, 'message': message})