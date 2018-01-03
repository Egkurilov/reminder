from flask import Flask, request
from .message import Message

app = Flask(__name__)

@app.route("/bot")
def bot_message():
    body = request.get_json()
    return Message(body)


