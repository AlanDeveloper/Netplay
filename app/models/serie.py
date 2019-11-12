from .. import db
from sqlalchemy import Column, Integer, String, Boolean

class serie(db.Model):
    __tablename__ = 'serie'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    synopsis = Column(String(1000), nullable=False)
    ageRange = Column(String(5), nullable=False)
    genero = Column(String(1000), nullable=False)
    image = Column(String(1000), nullable=False)
    season = Column(Integer, nullable=False)
    active = Column(Boolean, default=False, nullable=False)

    def __init__(self, title, synopsis, ageRange, genero, season, newname=None):
        self.title = title
        self.synopsis = synopsis
        self.ageRange = ageRange
        self.genero = genero
        self.season = season

        if newname:
            self.image = newname

    def add(serie):
        db.session.add(serie)
        db.session.commit()

    def ls():
        return serie.query.all()

    def delete(id):
        serie.query.filter_by(id=id).delete()
        db.session.commit()

    def update(serie):
        db.session.merge(serie)
        db.session.commit()

    def search(id):
        return serie.query.filter_by(id=id).first()

    def searchName(name):
        return serie.query.filter(serie.title.ilike('%'+name+'%')).all()
