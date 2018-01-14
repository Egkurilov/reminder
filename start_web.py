#!/usr/bin/env python3
from logging.config import dictConfig
import config

dictConfig(config.logging)
from flask import Flask
from app.routes import bot
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(bot)
app.config.from_object(config.Configuration)

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=True)
