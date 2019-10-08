from .. import db
from sqlalchemy import Column, Integer, String, ForeignKey

class film(db.Model):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    synopsis = Column(String(1000))
    ageRange = Column(Integer)

    def __init__(self, title, synopsis, ageRange):
        self.title = title
        self.synopsis = synopsis
        self.ageRange = ageRange

    def add(film):
        db.session.add(film)
        db.session.commit()

    def ls():
        return film.query.all()

    def delete(id):
        film.query.filter_by(id=id).delete()
        db.session.commit()

    def update(film):
        db.session.merge(film)
        db.session.commit()

    def search(id):
        return film.query.filter_by(id=id).first()
