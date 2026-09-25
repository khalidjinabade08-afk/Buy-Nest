from database.db import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "product"
    
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("sellers.id"), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500), nullable = True)
    price = db.Column(db.Numeric(10,2), nullable = False)
    quantity = db.Column(db.Integer, nullable = False, default = 0)
    image = db.Column(db.String(250), nullable = False)
    status = db.Column(db.String(20), nullable = False ,default = "active")
    discount = db.Column(db.Integer, nullable = False, default = 0)
    discount_start = db.Column(db.DateTime, nullable = True)
    discount_end = db.Column(db.DateTime, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)