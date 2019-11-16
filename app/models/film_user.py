from .. import db
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean

class film_user(db.Model):
    __tablename__ = 'film_user'
    film_id = Column(Integer, ForeignKey('film.id', ondelete='CASCADE'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    time = Column(String(1000))
    watched = Column(Boolean, default=False, nullable=False)
    
    users = db.relationship('user', backref='film_user')
    films = db.relationship('film', backref='film_user')

    def __init__(self, film_id, user_id, time):
        self.film_id = film_id
        self.user_id = user_id
        self.time = time

    def add(fu):
        db.session.add(fu)
        db.session.commit()

    def update(fu):
        db.session.merge(fu)
        db.session.commit()

    def search(video, id):
        return film_user.query.filter_by(film_id=video, user_id=id).first()

    def searchFilms(id):
        return film_user.query.filter_by(user_id=id).all()
