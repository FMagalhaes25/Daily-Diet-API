import os
from flask import Flask, request, jsonify
from models.refeicao import Refeicao
from dotenv import load_dotenv
from database import db

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')


db.init_app(app)


@app.route("/refeicao", methods=['POST'])
def criar_refeicao():
    data = request.json
    
    nome = data.get("nome")
    description = data.get("description")
    created_date = data.get("created_date")
    in_diet = data.get("in_diet")
    
    
    if nome:
        refeicao = Refeicao(nome=nome, description=description, created_date=created_date, in_diet=in_diet)
        db.session.add(refeicao)
        db.session.commit()
        return jsonify({"message": f"Refeição {nome} criada com sucesso"})
    
    return jsonify({"message": "Nome não pode ser nulo"}), 404
        
    
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
    

if __name__ == "__main__":
    app.run(debug=True)