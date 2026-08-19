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


if __name__ == "__main__":
    app.run(debug=True)