#!/usr/bin/env python3
import logging
from flask import Flask
from app.routes import bot


app = Flask(__name__)
app.register_blueprint(bot)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    app.run(host='localhost', port=88, debug=True)
