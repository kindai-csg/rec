#!/usr/bin/python3.6
# import cv2
import base64
# import threading
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit

# from record import recording_save_img

# capture = cv2.VideoCapture(0)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('live_1', namespace = '/')
def live_1():
    with open('/src/sample.jpg', 'rb') as f:
        emit('live_1', { 'data': base64.b64encode(f.read()).decode('ascii') })

@socketio.on('live_2', namespace = '/')
def live_2():
    with open('/src/sample.jpg', 'rb') as f:
        emit('live_2', { 'data': base64.b64encode(f.read()).decode('ascii') })

def main():
    # record_thread = threading.Thread(target=recording_save_img, args=(capture,))
    # record_thread.start()
    socketio.run(app, port=8080, debug=True, host='0.0.0.0')



if __name__ == '__main__':
    main()