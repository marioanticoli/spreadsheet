from flask_socketio import emit

from app.models import Cell
from app import socketio

@socketio.on('connect')
def on_connect():
    print("connected")
    emit("setvalues", Cell.list_last_values())


@socketio.on('disconnect')
def on_disconnect():
    print("disconnected")


@socketio.on("update")
def on_update(data):
    print(f"update {data['cell']}: {data['value']}")
    Cell.write_values(data['cell'], data['value'])
