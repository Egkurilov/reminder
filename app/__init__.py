import flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from config import logging, Configuration, host, port

dictConfig(logging)
from flask import Flask
from app.routes import bot


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

app.register_blueprint(bot)

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
