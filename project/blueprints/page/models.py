import datetime

from project.extensions import db
from lib.util_sqlalchemy import ResourceMixin


class Translate(ResourceMixin, db.Model):
    """ 
    Model to handle Translated texts
    """
    __tablename__ = 'translate'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(10), nullable=False, unique=True)
    original_text = db.Column(db.String(250), nullable=False)
    translated_text = db.Column(db.String(250), nullable=False)
    order_number = db.Column(db.Integer, unique=True)
    status = db.Column(db.String(20), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    
    def __init__(self, **kwargs):
        super(Translate, self).__init__(**kwargs)
