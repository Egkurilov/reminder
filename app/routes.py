from flask import Blueprint, request, jsonify
from .message import Message
import logging


bot = Blueprint('bot', __name__)
logger = logging.getLogger(__name__)


@bot.route("/bot", methods=['POST'])
def bot_message():
    body = request.get_json()
    message = Message(body)
    logger.debug(repr(message))

    return jsonify(body)