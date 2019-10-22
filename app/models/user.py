from .. import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class user(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    typeAdmin = Column(Boolean, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.type = False

    def add(u):
        db.session.add(u)
        db.session.commit()

    def ls():
        return user.query.all()

    def delete(id):
        user.query.filter_by(id=id).delete()
        db.session.commit()

    def update(u):
        db.session.merge(u)
        db.session.commit()

    def search(id):
        return user.query.filter_by(id=id).first()
