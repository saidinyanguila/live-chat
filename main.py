from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_login import current_user
from flask import request
from website import create_app
import random

app = create_app()

socketio = SocketIO(app)
users = {}

@socketio.on('join')
def handle_join(room_name):
    join_room(room_name)
    emit("user_join", {"user": current_user.username}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid, "Anonymous")  # Get the user's name
    emit("message", {"user" :current_user.username, "color": f"rgb({current_user.col_r},{current_user.col_g},{current_user.col_b})","message" :data}, broadcast=True)  # Send to everyone

# Handle disconnects
@socketio.on('disconnect')
def handle_disconnect():
    username = users.pop(request.sid, "Anonymous")
    emit("user_left", {"user": current_user.username}, broadcast=True)



if __name__ == '__main__' :
 	app.run(debug=True, host='0.0.0.0', port=5000)


