from flask import Flask, request
from .message import Message
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/bot", methods=['GET', 'POST'])
def bot_message():
    body = request.get_json()
    logger.debug(repr(body))
    return Message(body)
