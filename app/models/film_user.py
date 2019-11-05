from .. import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class film_user(db.Model):
    __tablename__ = 'film_user'
    film_id = Column(Integer, ForeignKey('film.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    time = Column(Integer)
    
    users = db.relationship('user', backref='film_user')
    films = db.relationship('film', backref='film_user')

    def __init__(self, film_id, user_id, time):
        self.film_id = film_id
        self.user_id = user_id
        self.time = time

    def add(fu):
        db.session.add(fu)
        db.session.commit()
