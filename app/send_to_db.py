# TODO класс общения с БД
from app import db


class Messagedb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
