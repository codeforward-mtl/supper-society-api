from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

   # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
   # store = db.relationship('StoreModel')

    def __init__(self, name):
        self.name = name
       # self.store_id = store_id

    def json(self):
        return {'name': self.name, 'id': self.id}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()