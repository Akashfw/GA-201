from flask import Flask, render_template
from flask_socketio import SocketIO


app= Flask(__name__)
app.config['key']="akash"
socketio= SocketIO(app)


