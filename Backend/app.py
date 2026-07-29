from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
import os

from config import config as ConfigClass
from database.db import db
from extensions import mail

# Models
from models.user import User
from models.OTP import OTP

# Routes
from routes.user_routes import auth_routes

load_dotenv()

app = Flask(__name__)
app.config.from_object(ConfigClass)
app.secret_key = os.getenv("SECRET_KEY")

db.init_app(app)
mail.init_app(app)

api = Api(
    app,
    title="E-Commers Sysrem API",
    version="1.0",
    description="E-commers webside",
    doc="/swagger",
)

api.add_namespace(auth_routes, path="/auth")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2488, debug=True)
