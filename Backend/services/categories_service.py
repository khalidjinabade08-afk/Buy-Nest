import os
import uuid

from werkzeug.utils import secure_filename
from database.db import db
from models.categories import Category
from utils.response import error_response, success_response

UPLOAD_FOLDER = "uploads/categories"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def create_category(data, image=None):
    try:
        name = data.get("name")
        description = data.get("description")
        status = data.get("status") or "Available"

        if not name:
            return error_response(
                "Category name is required.",
                400
            )

        name = name.strip()

        existing_category = Category.query.filter(
            db.func.lower(Category.name) == name.lower()
        ).first()

        if existing_category:
            return error_response(
                "Category already exists.",
                400
            )

        status = status.strip().lower()

        allowed_status = {
            "available": "Available",
            "unavailable": "Unavailable"
        }

        if status not in allowed_status:
            return error_response(
                "Status must be Available or Unavailable.",
                400
            )

        status = allowed_status[status]

        if description:
            description = description.strip()


        image_filename = None
        image_path = None

        if image:
            if not image.filename:
                return error_response(
                    "Invalid category image.",
                    400
                )

            if not allowed_file(image.filename):
                return error_response(
                    "Only PNG, JPG, JPEG and WEBP files are allowed.",
                    400
                )

            os.makedirs(
                UPLOAD_FOLDER,
                exist_ok=True
            )

            safe_filename = secure_filename(
                image.filename
            )

            extension = safe_filename.rsplit(
                ".",
                1
            )[1].lower()

            image_filename = (
                f"{uuid.uuid4().hex}.{extension}"
            )

            image_path = os.path.join(
                UPLOAD_FOLDER,
                image_filename
            )

            image.save(image_path)

        new_category = Category(
            name=name,
            description=description,
            image=image_filename,
            status=status
        )

        db.session.add(new_category)
        db.session.commit()

        return success_response(
            "Category created successfully.",
            {
                "id": new_category.id,
                "name": new_category.name,
                "description": new_category.description,
                "image": new_category.image,
                "status": new_category.status,
                "created_at": (
                    new_category.created_at.isoformat()
                    if new_category.created_at
                    else None
                )
            },
            201
        )

    except Exception as e:
        db.session.rollback()

        if image_path and os.path.exists(image_path):
            os.remove(image_path)

        return error_response(
            f"Category not created: {str(e)}",
            500
        )
            
def get_all_categories():
    try:
        categories = Category.query.all()
        if not categories:
            return error_response(
                "No categories found", 404
            )
        category_list = []
        
        for category in categories:
            category_list.append({
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "image": category.image,
                "status": category.status,
                "created_at": (
                    category.created_at.isoformat()
                    if category.created_at
                    else None
                ),
                "updated_at": (
                    category.updated_at.isoformat()
                    if category.updated_at
                    else None
                )
            })
            
        return success_response(
            "Categories fetched successfully.",
            category_list,200
        )
    except Exception as e:
        return error_response(
            f"An error occurred: {str(e)}",500
        )
        
def get_category_by_id(category_id):
    try:
        category = db.session.get(Category, category_id)
        
        if not category:
            return error_response("Category not found.", 404)
        
        category_data = {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "image": category.image,
            "status": category.status,

            "created_at": (
                category.created_at.isoformat()
                if category.created_at
                else None
            ),

            "updated_at": (
                category.updated_at.isoformat()
                if category.updated_at
                else None
            )
        }
        
        return success_response(
            "Category fetched successfully.", category_data, 200
        )

    except Exception as e:
        return{
            "message": "category not found",
            "error": str(e)
        }
        
def update_category(category_id, data, image=None):
    try:
        category = db.session.get(Category, category_id)
        
        if not category:
            return error_response("Category not found.", 404)
        
        name = data.get("name")
        description = data.get("description")
        
        if name:
            name = name.strip()
            existing_category = Category.query.filter(
                db.func.lower(Category.name) == name.lower(),
                category.id != category_id
            ).first()
            
            if existing_category:
                return error_response("Category name already exists."),400
            
            category.name = name
            
            if description is not None:
                category.description = description
                
            if image:
                if not image.filename:
                    return error_response("Invalid category image.",400)
                
                if not allowed_file(image.filename):
                    return error_response("Only PNG, JPG, JPEG and WEBP files are allowed.",400)
                
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                safe_filename = secure_filename(image.filename)
                extension = safe_filename.rsplit(".",1)[1].lower()
                
                image_filename = f"{uuid.uuid4().hex}.{extension}"
                image_path = os.path.join(UPLOAD_FOLDER, image_filename)
                image.save(image_path)
                
                if category.image:
                    old_image_path = os.path.join(UPLOAD_FOLDER, category.image)
                    
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
                        
                category.image = image_filename
                
            db.session.commit()
                
            return success_response(
                "Category updated successfully.",
                {
                    "id": category.id,
                    "name": category.name,
                    "description": category.description,
                    "image": category.image,
                    "status": category.status
                },200
                )
    except Exception as e:
        db.session.rollback()
        return{
            "message": "category update failed",
            "error": str(e)
        }

def update_category_status(category_id, data):
    try:
        category = db.session.get(Category, category_id)
        
        if not category:
            return error_response("category not found.",404)
        
        status = data.get("status")
        
        if not status:
            return error_response("Status is required.", 400)
        
        allowed_status = ["Available", "Unavailable"]
        
        if status not in allowed_status:
            return error_response("Status must be Available or Unavailable.")
        
        category.status = status
        
        db.session.commit()
        
        return success_response(
            "Category status updated successfully.",
            {
                "id": category.id,
                "name": category.name,
                "status": category.status
            }, 200
        )
    
    except Exception as e:
        db.session.rollback()
        return{
            "message": "category status updated failed.",
            "error": str(e)
        }
        
def delete_category(category_id):
    try:
        category = db.session.get(Category, category_id)
        
        if not category:
            return error_response("Category not found.", 404)
        
        image_name = category.image
        
        db.session.delete(category)
        db.session.commit()
        
        if image_name:
            image_path = os.path.join(UPLOAD_FOLDER, image_name)
            
            if os.path.exists(image_path):
                os.remove(image_path)
                
        return success_response("Category deleted successfully.", None, 200)
    
    except Exception as e:
        db.session.rollback()
        return{
            "Message:": "Category deleted dailed.",
            "error": str(e)
        }