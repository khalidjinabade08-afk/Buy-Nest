import os
import uuid

from werkzeug.utils import secure_filename
from database.db import db
from models.Sellers import Seller
from utils.response import success_response, error_response

UPLOAD_FOLDER = "uploads/seller_logos"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def create_seller(data, user_id, shop_logo):
    try:
        existing_seller = Seller.query.filter_by(user_id=user_id).first()
        
        if existing_seller:
            return error_response("Seller profile already exists for this user.", 400)
        
        shop_name = data.get("shop_name")
        if not shop_name:
            return error_response("Shop name is required.", 400)
        
        logo_filename = None
        
        if shop_logo:
            if not allowed_file(shop_logo.filename):
                return error_response("Only PNG, JPG, JPEG, and WEBP files are allowed for shop logo.", 400)
            
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            safe_filename = secure_filename(shop_logo.filename)
            extension = safe_filename.rsplit(".", 1)[1].lower()
            logo_filename = f"{uuid.uuid4().hex}.{extension}"
            logo_path = os.path.join(UPLOAD_FOLDER, logo_filename)
            shop_logo.save(logo_path)
                  
        new_seller = Seller(
            user_id=user_id,
            shop_name=shop_name,
            shop_logo=logo_filename if shop_logo else None,
            shop_description=data.get("shop_description"),
            shop_address=data.get("shop_address")
        )

        db.session.add(new_seller)
        db.session.commit()

        return success_response(
            "Seller profile created successfully.",
            {
                "seller_id": new_seller.id,
                "shop_name": new_seller.shop_name,
                "shop_logo": new_seller.shop_logo,
                "status": new_seller.status
             },
            201
        )

    except Exception as e:
        db.session.rollback()
        return error_response(f"An error occurred: {str(e)}", 500)

def get_seller(user_id):
    seller = Seller.query.filter_by(user_id=user_id).first()
    
    if not seller:
        return{
            "message": "Seller profile not found."
        },404
        
    return{
        "Seller":{
            "id":seller.id,
            "user_id":seller.user_id,
            "shop_name":seller.shop_name,
            "shop_logo": seller.shop_logo,
            "shop_description":seller.shop_description,
            "shop_address":seller.shop_address,
            "status":seller.status,
            "created_at":seller.created_at.isoformat(),
            "updated_at":seller.updated_at.isoformat()
        }
    }, 200

def update_seller(user_id, data, shop_logo):
    try:
        seller = Seller.query.filter_by(user_id=user_id).first() 
        
        if not seller:
            return {
                "message": "Seller profile not found"
            }, 404
        
        if data.get("shop_name"):
            seller.shop_name = data.get("shop_name")
            
        if data.get("shop_description"):
            seller.shop_description = data.get("shop_description")
            
        if data.get("shop_address"):
            seller.shop_address = data.get("shop_address")
        
        if shop_logo:
            if not shop_logo.filename:
                return error_response(
                    "Invalid shop logo", 400
                )
                
            if not allowed_file(shop_logo.filename):
                return error_response(
                    "Only PNG, JPG, JPEG, and WEBP files are allowed for shop logo.", 400
                )
                
            os.makedirs(
                UPLOAD_FOLDER,exist_ok=True
            )
            
            safe_filename = secure_filename(
                shop_logo.filename
            )
            
            extension = safe_filename.rsplit(
                ".",
                1
            )[1].lower()
            
            logo_filename = (
                f"{uuid.uuid4().hex}.{extension}"
            )
            
            logo_path = os.path.join(
                UPLOAD_FOLDER,
                logo_filename
            )
            
            shop_logo.save(logo_path)
            
            seller.shop_logo = logo_filename
        
        db.session.commit()
        
        return {
            "message": "Seller profile updated successfully",
            "seller": {
                "id": seller.id,
                "shop_name": seller.shop_name,
                "shop_logo": seller.shop_logo,
                "shop_description": seller.shop_description,
                "shop_address": seller.shop_address,
                "status": seller.status,
                "updated_at": seller.updated_at.isoformat()
            }
        }
    except Exception as e:
        db.session.rollback()
        
        return error_response(
            f"an error occured: {str(e)}",
            500
        )
  
def update_seller_status(seller_id, data):
    try:
        seller = Seller.query.get(seller_id)
        
        if not seller:
            return{
                "message": "Seller not found"
            }, 404
            
        status= data.get("status")
        
        if not status:
            return {
                "message": "Status is required"
            }, 400
            
        status = status.strip().lower()
        
        allowed_status = ["pending" , "approved" , "rejected" , "blocked"]
        
        if status not in allowed_status:
            return{
                "message": "Invalid seller status"
            }, 400
            
        seller.status = status
        
        db.session.commit()
        
        return{
            "message": "Seller status updated successfully",
            "seller_id": seller.id,
            "status": seller.status 
        }, 200
    except Exception as e:
        db.session.rollback()
        
        return{
            "message": "Failed to update seller status",
            "error": str(e)
        }, 500

def delete_seller(seller_id):
    try:
        seller = Seller.query.get(seller_id)
        
        if not seller:
            return{
                "message": "Seller not found"
            }, 404
            
        db.session.delete(seller)
        db.session.commit()
        
        return {
            "message": "seller deleted successfully"
        }, 200
    except Exception as e:
        db.session.rollback()
        return{
            "message": "Failed to delete seller",
            "error": str(e)
        }, 200