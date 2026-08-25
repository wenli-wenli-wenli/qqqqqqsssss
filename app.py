from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# 允许跨域
socketio = SocketIO(app, cors_allowed_origins="*")

# 收到前端chat事件，广播所有人
@socketio.on('chat')
def handle_chat(text):
    print("收到消息：", text)
    socketio.emit('chat', text, broadcast=True)

if __name__ == '__main__':
    # host 0.0.0.0 对外开放端口，render部署必须这样写
    socketio.run(app, host="0.0.0.0", debug=False)

