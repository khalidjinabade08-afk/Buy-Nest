import os
import uuid
from werkzeug.utils import secure_filename
from datetime import datetime

from database.db import db
from models.Product import Product
from models.Sellers import Seller
from models.categories import Category
from utils.response import success_response, error_response


UPLOAD_FOLDER = "uploads/Product_image"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def create_product(data, user_id, image):
    seller = Seller.query.filter_by(user_id = user_id).first()
        
    if not seller:
        return{
            "message": "seller profile not found."
        }, 404
            
    if seller.status != "approved":
        return{
            "message": "Your seller account is not approved."
        }, 403
            
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    quantity = data.get("quantity")
    category_id = data.get("category_id")
    discount = data.get("discount", 0)
    discount_start = data.get("discount_start")
    discount_end = data.get("discount_end")
        
    if not name:
        return{
            "message": "Product name is required."
        }, 400
        
    if not category_id:
        return{
            "message": "Category is required."
        }, 400
        
    if price is None:
        return{
            "message": "Price is required."
        }, 400
        
    if quantity is None:
        return{
            "message": "Quantity is required."
        }, 400
            
    category = db.session.get(Category, category_id)
        
    if not category:
        return {
            "message": "Category not found."
        }, 404
            
    if category.status != "Available":
        return{
            "message": "This category is not Available"
        }, 400
        
    try:
        price = float(price)
        
        if price <= 0:
            return{
                "message": "Price must be greater than 0"
            }, 400
        
    except (ValueError, TypeError):
        return{
            "message": "Invalid price"
        }, 400
        
    try:
        quantity = int(quantity)
        
        if quantity < 0:
            return{
                "messsage": "Qoantity cannot be negative"
            }, 400
            
    except(ValueError, TypeError):
        return{
            "message": "invalid quantity"
        }, 400
        
    try:
        discount = int(discount or 0)
        
        if discount < 0 or discount > 100:
            return{
                "message": "Discount must be between 0 and 100"
            }, 400
            
    except (ValueError, TypeError):
        return {
            "message": "invalid discount"
        }, 400
    
    if not image or image.filename == "":
        return{
            "message": "Product image is required" 
        }, 400
        
    if not allowed_file(image.filename):
        return{
            "message": "Only png, jpg, jpeg and webp image are allowed."
        }, 400
        
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    original_filename = secure_filename(image.filename)
    extension = original_filename.rsplit(".", 1)[1].lower()
    new_filename = f"{uuid.uuid4().hex}.{extension}"
    
    image_path = os.path.join(UPLOAD_FOLDER, new_filename)
    image.save(image_path)
    
    try:
        if discount_start:
            discount_start = datetime.fromisoformat(str(discount_start))
        
        if discount_end:
            discount_end = datetime.fromisoformat(str(discount_end))
    except ValueError:
        return{
            "message": "Invalid discount date format. Use YYYY-MM-DD"
        }, 400
    
    if discount_start and discount_end:
        if discount_end <= discount_start:
            return{
                "message": "Discount end date must be after start date"
            }, 400
    
    try:
        
        product = Product(
            seller_id = seller.id,
            category_id = category.id,
            name = name,
            description = description,
            price = price,
            quantity = quantity,
            image = new_filename,
            status = "active",
            discount = discount,
            discount_start = discount_start,
            discount_end = discount_end
        )
        
        db.session.add(product)
        db.session.commit()
        
        return {
            "message": "Product created successfully",

            "product": {
                "id": product.id,
                "seller_id": product.seller_id,
                "category_id": product.category_id,
                "name": product.name,
                "description": product.description,
                "price": float(product.price),
                "quantity": product.quantity,
                "image": product.image,
                "status": product.status,
                "discount": product.discount,

                "discount_start": (
                    product.discount_start.isoformat()
                    if product.discount_start
                    else None
                ),

                "discount_end": (
                    product.discount_end.isoformat()
                    if product.discount_end
                    else None
                )
            }
        }, 201

    except Exception as e:
        db.session.rollback()
        if os.path.exists(image_path):
            os.remove(image_path)
        return {
            "message": "Failed to create product.",
            "error": str(e)
        }, 500