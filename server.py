#!/usr/bin/python3.6
import base64
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('live_1', namespace = '/')
def live_1():
    with open('/home/recorder/public/latest127.0.0.1.jpg', 'rb') as f:
        emit('live_1', { 'data': base64.b64encode(f.read()).decode('ascii') })

@socketio.on('live_2', namespace = '/')
def live_2():
    with open('/home/recorder/public/latest172.24.18.2.jpg', 'rb') as f:
        emit('live_2', { 'data': base64.b64encode(f.read()).decode('ascii') })

def main():
    socketio.run(app, port=8080, debug=True, host='0.0.0.0')

if __name__ == '__main__':
    main()