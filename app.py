from flask import Flask
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")
@socketio.on('chat')
def receive_chat(message):
    socketio.emit('chat', message,broadcast=True)
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',debug=False,allow_unsafe_werkzeug=True)
