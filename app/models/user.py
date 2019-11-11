import hashlib
from .. import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class user(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    typeAdmin = Column(Boolean, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        h = hashlib.md5(password.encode())
        self.password = h.hexdigest()
        self.typeAdmin = False

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

    def search(email, password):
        password = hashlib.md5(password.encode())
        u = user.query.filter_by(
            email=email, password=password.hexdigest()).first()
        return u
