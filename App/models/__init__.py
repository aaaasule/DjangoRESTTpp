# -*- encoding: utf-8 -*-
from App.ext import db


class ModelBase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def update(self):
        try:
            db.session.update(self)
            db.session.commit()
            return True
        except:
            return False
