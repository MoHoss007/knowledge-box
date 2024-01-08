from flask_sqlalchemy import SQLAlchemy
from knowledge_box.extensions import db


class Passage(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    topic = db.Column(db.String(length=50), nullable=False)
    title = db.Column(db.String(length=50), nullable=False, unique=True)
    text = db.Column(db.String(length=4000), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
