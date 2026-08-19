from database import db
from sqlalchemy.sql import func

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    in_diet = db.Column(db.Boolean, default=True)