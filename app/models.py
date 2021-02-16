import datetime

from app import db

class Cell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cell = db.Column(db.String(2), index=True)
    content = db.Column(db.String())
    created = db.Column(db.DateTime(timezone=False), default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<{}: {}>'.format(self.cell, self.content)    
