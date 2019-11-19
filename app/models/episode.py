from .. import db
from sqlalchemy import Column, Integer, String, Boolean

class episode(db.Model):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    serieId = Column(Integer, nullable=False)
    seasonNumber = Column(Integer, nullable=False)
    video = Column(String(1000), nullable=False)

    def __init__(self, title, serieId, seasonNumber, newname=None):
        self.title = title
        self.serieId = serieId
        self.seasonNumber = seasonNumber
        self.video = newname

    def add(episode):
        db.session.add(episode)
        db.session.commit()

    def ls():
        return episode.query.all()

    def delete(id):
        episode.query.filter_by(id=id).delete()
        db.session.commit()

    def update(episode):
        db.session.merge(episode)
        db.session.commit()

    def search(serie_id, season_id):
        return episode.query.filter_by(
            serieId = serie_id,
            seasonNumber = season_id
        ).all()
    
    def search_episode(serie_id, season_id, episode_id):
        return episode.query.filter_by(
            serieId=serie_id,
            seasonNumber=season_id,
            id=episode_id
        ).first()

    def searchName(name):
        return episode.query.filter(episode.title.ilike('%'+name+'%')).all()
