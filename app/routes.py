from flask import Blueprint, request
from .message import Message
import logging

bot = Blueprint('bot', __name__)
logger = logging.getLogger(__name__)


@bot.route("/bot", )
def bot_message():
    body = request.get_json()
    logger.debug(str(body))
    message = Message(body)
    logger.debug(repr(message))
    return message
