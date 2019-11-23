from .. import db
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean

class serie_user(db.Model):
    __tablename__ = 'serie_user'
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    episode_id = Column(Integer, ForeignKey('episode.id', ondelete='CASCADE'), primary_key=True)
    serie_id = Column(Integer, ForeignKey('serie.id', ondelete='CASCADE'), primary_key=True)
    season_id = Column(Integer, nullable=False)
    time = Column(String(1000), nullable=False)
    watched = Column(Boolean, default=False, nullable=False)
    
    users = db.relationship('user', backref='serie_user')
    series = db.relationship('serie', backref='serie_user')
    episodes = db.relationship('episode', backref='serie_user')

    def __init__(self, serie_id, season_id, episode_id, user_id, time):
        self.serie_id = serie_id
        self.season_id = season_id
        self.episode_id = episode_id
        self.user_id = user_id
        self.time = time

    def add(su):
        db.session.add(su)
        db.session.commit()

    def update(su):
        db.session.merge(su)
        db.session.commit()

    def search(se, sea, video, id):
        return serie_user.query.filter_by(
            user_id=id, episode_id=video, serie_id=se, season_id=sea
        ).first()

    def searchseries(id):
        return serie_user.query.filter_by(user_id=id).all()
