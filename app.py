from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "chat backend ok"

@socketio.on('chat')
def handle_chat(text):
    print("收到消息：", text)
    socketio.emit('chat', text, broadcast=True)

# 注意：这里不要写 socketio.run ！！
