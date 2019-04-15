from flask import Flask, render_template, request, redirect, session, flash
from flask_socketio import SocketIO
# from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

# @socketio.on('message')
# def handle_message(message):
#     print('received message: ' + message)
#     socketio.emit('apple', message, broadcast=True)

@socketio.on('banana')
#banana is the event handler 
def handle_message(message):
    # print(type(message))
    print(message['data'])
    # print('received message: ' + message['data'])
    socketio.emit('apple', message['data'], broadcast=True)
    # emits to all open sockets
    
# @socketio.on('json')
# def handle_json(json):
#     send(json, json=True)

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     emit('my response', json)


if __name__ == "__main__":
    socketio.run(app)