# Daily Diet API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1.3-000000?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/MySQL-8-4479A1?logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white" alt="Docker Compose">
</p>

API REST para controle de refeições e acompanhamento da dieta diária. O projeto foi desenvolvido com Flask, utiliza Flask-SQLAlchemy para persistência e disponibiliza um CRUD completo de refeições.

## Funcionalidades

- Criar uma refeição
- Listar todas as refeições
- Consultar uma refeição pelo ID
- Editar uma refeição existente
- Excluir uma refeição
- Registrar se a refeição está dentro da dieta
- Persistir os dados em um banco MySQL executado via Docker Compose

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- MySQL
- PyMySQL
- python-dotenv
- Docker Compose

## Pré-requisitos

- Python 3.13 ou superior
- Docker e Docker Compose
- Git

## Como executar

1. Clone o repositório e entre na pasta do projeto:

	```bash
	git clone https://github.com/FMagalhaes25/Daily-Diet-API.git
	cd Daily-Diet-API
	```

2. Crie e ative um ambiente virtual:

	```bash
	python -m venv venv
	```

	No Windows:

	```powershell
	.\venv\Scripts\Activate.ps1
	```

	No Linux/macOS:

	```bash
	source venv/bin/activate
	```

3. Instale as dependências:

	```bash
	pip install -r requirements.txt
	```

4. Configure as variáveis de ambiente. Copie `.env-example` para `.env` e preencha:

	```env
	SECRET_KEY=sua-chave-secreta
	SQLALCHEMY_DATABASE_URI=mysql+pymysql://admin:admin1234@127.0.0.1:3306/flask-daily-diet
	```

5. Suba o banco de dados:

	```bash
	docker compose up -d
	```

6. Inicie a API:

	```bash
	python app.py
	```

A API ficará disponível em `http://127.0.0.1:5000`.

Para desligar o banco, execute:

```bash
docker compose down
```

## Endpoints

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `POST` | `/refeicao` | Cria uma refeição |
| `GET` | `/refeicao` | Lista todas as refeições |
| `GET` | `/refeicao/<id>` | Busca uma refeição pelo ID |
| `PUT` | `/refeicao/<id>` | Atualiza uma refeição |
| `DELETE` | `/refeicao/<id>` | Remove uma refeição |

### Criar uma refeição

Requisição:

```http
POST /refeicao
Content-Type: application/json
```

```json
{
  "nome": "Arroz, feijão e frango",
  "description": "Refeição do almoço",
  "in_diet": true
}
```

Resposta:

```json
{
  "message": "Refeição Arroz, feijão e frango criada com sucesso"
}
```

### Atualizar uma refeição

```http
PUT /refeicao/1
Content-Type: application/json
```

```json
{
  "nome": "Arroz integral, feijão e frango",
  "description": "Almoço atualizado",
  "in_diet": true
}
```

## Modelo de dados

Cada refeição possui os seguintes campos:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `id` | Integer | Identificador único |
| `nome` | String | Nome da refeição, obrigatório |
| `description` | String | Descrição da refeição |
| `created_date` | DateTime | Data e hora de criação, gerada pelo banco |
| `in_diet` | Boolean | Indica se a refeição faz parte da dieta |

## Estrutura do projeto

```text
Daily-Diet-API/
├── app.py                  # Rotas e inicialização da API
├── database.py             # Configuração do Flask-SQLAlchemy
├── docker-compose.yaml     # Serviço MySQL
├── models/
│   └── refeicao.py         # Modelo da refeição
├── requirements.txt        # Dependências Python
├── .env-example            # Exemplo de configuração
└── README.md
```

## Observações

- O arquivo `.env` contém configurações locais e não deve ser versionado.
- O banco utiliza a porta `3306` por padrão.
- A aplicação inicia em modo de desenvolvimento com `debug=True`.
