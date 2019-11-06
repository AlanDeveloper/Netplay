from .. import db
from sqlalchemy import Column, Integer, String

class film(db.Model):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    synopsis = Column(String(1000), nullable=False)
    ageRange = Column(String(5), nullable=False)
    image = Column(String(1000), nullable=False)
    video = Column(String(1000), nullable=False)

    def __init__(self, title, synopsis, ageRange, image = None, video = None):
        self.title = title
        self.synopsis = synopsis
        self.ageRange = ageRange
        if image:
            self.image = image
        if video:
            self.video = video

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
