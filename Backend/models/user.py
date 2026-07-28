from database.db import db
from sqlalchemy.orm import validates
import re


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(250), default="customer")
    
    @validates("email")
    def validate_email(self, key, email):
        if not email.lower().endswith("@gmail.com"):
            raise ValueError("Only Gmail addresses are allowed.")
        return email