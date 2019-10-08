from app import db
#devo tirar o not null de sericod e adiconar altura
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100),  nullable=False)
    email = db.Column(db.String(100),  nullable=False)
    tipo = db.Column(db.String(10),  nullable=False)
