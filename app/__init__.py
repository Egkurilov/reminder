from flask import app, config
from flask_sqlalchemy import SQLAlchemy

app.config.from_object(config.Configuration)
db = SQLAlchemy(app)