from database.db import db
from sqlalchemy.orm import validates
from datetime import datetime
import re


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(250), default="customer")
    status = db.Column(db.String(250), default="active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @validates("email")
    def validate_email(self, key, email):
        if not email.lower().endswith("@gmail.com"):
            raise ValueError("Only Gmail addresses are allowed.")
        return email