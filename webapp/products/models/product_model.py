from db.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), unique=False, nullable=False)
    section = db.Column(db.String(100), unique=False, nullable=False)

    def __init__(self, name, owner, section):
        self.name = name
        self.owner = owner
        self.section =  section