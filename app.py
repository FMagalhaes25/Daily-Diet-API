import os
from flask import Flask, request, jsonify
from models.user import User
from models.refeicao import Refeicao
from dotenv import load_dotenv
from database import db

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')


db.init_app(app)

        
    
@app.route("/refeicao/<int:id_refeicao>", methods=['PUT'])
def editar_refeicao(id_refeicao):
    data = request.json
    refeicao = Refeicao.query.get(id_refeicao)
    
    if refeicao:
        refeicao.nome = data.get("nome")
        refeicao.description = data.get("description")
        refeicao.in_diet = data.get("in_diet")
        
        db.session.commit()
        
        return jsonify({"message": "Refeição editada com sucesso!"})
    
    return jsonify({"message": "Refeição não encontrada"})


@app.route("/refeicao/<int:id_refeicao>", methods=['DELETE'])
def deletar_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)
    
    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()
        
        return jsonify({"message": "Refeição deletada com sucesso!"})
    
    return jsonify({"message": "Refeição não encontrada"})

@app.route("/refeicao")
def visualizar_refeicoes():
    refeicoes = Refeicao.query.all()
    
    lista_refeicoes = []
    
    for refeicao in refeicoes:
        lista_refeicoes.append({
            "id": refeicao.id,
            "nome": refeicao.nome,
            "description": refeicao.description,
            "created_date": refeicao.created_date,
            "in_diet": refeicao.in_diet
        })
    
    return jsonify(lista_refeicoes)


@app.route("/refeicao/<int:id_refeicao>", methods=['GET'])
def visualizar_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)
    
    if refeicao:
        return jsonify({
            "nome": refeicao.nome,
            "description": refeicao.description,
            "in_diet": refeicao.in_diet,
            "created_date": refeicao.created_date
        })
        
    return jsonify({"message": "Refeição não encontrada"})
    

@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()
    
    name = data.get("name")
    password = data.get("password")
    
    if not name or not password:
        return jsonify({"message": "Nome e senha são obrigatórios"}), 400
    
    new_user = User(name=name, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "Usuário criado com sucesso!", "user": new_user.to_dict()}), 201


@app.route("/user/<int:user_id>/refeicao", methods=['POST'])
def create_refeicao(user_id):
    user = db.session.get(User, user_id)
    
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404
        
    data = request.get_json()
    nome = data.get("nome")
    
    if not nome:
         return jsonify({"message": "O nome da refeição é obrigatório"}), 400
         
    nova_refeicao = Refeicao(
        nome=nome,
        description=data.get("description", ""),
        in_diet=data.get("in_diet", True),
        user_id=user.id
    )
    
    db.session.add(nova_refeicao)
    db.session.commit()
    
    return jsonify({"message": "Refeição cadastrada!", "refeicao": nova_refeicao.to_dict()}), 201

@app.route("/user/<int:id_user>/refeicoes", methods=['GET'])
def refeicao_by_user(id_user):
    user = db.session.get(User, id_user)
    
    if not user:
        return jsonify({"message": "Não existe este usuário"}), 404
    
    refeicoes_list = [refeicao.to_dict() for refeicao in user.refeicoes]
    
    return jsonify({"Refeições": refeicoes_list})
    

if __name__ == "__main__":
    app.run(debug=True)