# TODO класс общения с БД
from routes import db


class Messagedb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
