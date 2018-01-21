from app import db


class MessageDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
