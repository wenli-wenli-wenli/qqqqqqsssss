# 必须写在所有import最开头！！！
from gevent import monkey
monkey.patch_all()

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# 强制指定async_mode为gevent
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="gevent")

@app.route('/')
def index():
    return "chat backend ok"

@socketio.on('chat')
def handle_chat(text):
    print("收到消息：", text)
    socketio.emit('chat', text, broadcast=True)

# 删掉 if __name__ == '__main__': socketio.run(...)
