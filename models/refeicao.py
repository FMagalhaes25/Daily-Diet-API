from database import db
from sqlalchemy.sql import func

class Refeicao(db.Model):
    __tablename__ = 'refeicoes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    in_diet = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "description": self.description,
            "created_date": self.created_date.isoformat() if self.created_date else None, 
            "in_diet": self.in_diet,
            "user_id": self.user_id
        }