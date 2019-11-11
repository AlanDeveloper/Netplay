from .. import db
from sqlalchemy import Column, Integer, String, Boolean

class film(db.Model):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    synopsis = Column(String(1000), nullable=False)
    ageRange = Column(String(5), nullable=False)
    image = Column(String(1000), nullable=False)
    video = Column(String(1000), nullable=False)
    active = Column(Boolean, default=False, nullable=False)

    def __init__(self, title, synopsis, ageRange, newname=None, newname2=None):
        self.title = title
        self.synopsis = synopsis
        self.ageRange = ageRange

        if newname:
            self.image = newname
        if newname2:
            self.video = newname2

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

    def searchName(name):
        return film.query.filter(film.title.ilike('%'+name+'%')).all()
