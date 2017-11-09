"""
This script performs density estimation for randomly generated data.
In contrast to "offline.py", it computes density progressively, using the
'run' method of PANENE.

To see the result, run this script with Python 3, Flask, and Flask-SocketIO
(we recommend to use Anaconda 3). Then, open 'localhost:8001' on your browser.
"""


from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='')
app.config['SECRET_KEY'] = 'your secret key'
socketio = SocketIO(app)

html = "dddr가나다라"

@app.route('/')
def main():
    return app.send_static_file('index.html')

@app.route('/edit')
def edit():
    return app.send_static_file('edit.html')

@socketio.on('connect')
def connect():
    emit('update', html)
    
@socketio.on('edit')
def edited(nhtml):
    global html
    html = nhtml
    socketio.emit('update', html, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
