from flask_restx import Namespace, Resource, reqparse, fields
from flask import session
from werkzeug.datastructures import FileStorage

from services.categories_service import create_category, get_all_categories, get_category_by_id, update_category, update_category_status, delete_category

category_routes = Namespace("Category API", description="Category Management APIs")

# =============== create category =========================
category_create_model = reqparse.RequestParser()
category_create_model.add_argument(
    "name",
    type=str,
    required=True,
    location = "form",
    help = "Category name is required"
)

category_create_model.add_argument(
    "description",
    type=str,
    required=False,
    location="form"
)

category_create_model.add_argument(
    "image",
    type=FileStorage,
    required=False,
    location="files"
)

category_create_model.add_argument(
    "status",
    type=str,
    required=False,
    location="form",
    help = "Available / Unavailable"
)

# ===========update category ==============
category_update_model = reqparse.RequestParser()

category_update_model.add_argument(
    "name",
    type=str,
    required=False,
    location="form"
)

category_update_model.add_argument(
    "description",
    type=str,
    required=False,
    location="form"
)

category_update_model.add_argument(
    "image",
    type=FileStorage,
    required=False,
    location="files"
)

category_status_model = category_routes.model(
    "CategoryStatus",
    {
        "status": fields.String(
            required = True,
            description = "Available / Unavailable"
        )
    }
)

@category_routes.route("/create")
class CreateCategory(Resource):
    @category_routes.expect(category_create_model)
    def post(self):
        if not session.get("user_id"):
            return{
                "message": "Please login first"
            }, 401
        
        # if session.get("role") != "admin":
        #     return {
        #         "message": "Admin access required"
        #     }, 403
            
        data = category_create_model.parse_args()
        
        image = data.get("image")
        
        return create_category(data, image)
    
@category_routes.route("/all")
class GetAllCategories(Resource):
    def get(self):
        return get_all_categories()
    
@category_routes.route("/<int:category_id>")
class GetCategoryById(Resource):
    def get(self, category_id):
        return get_category_by_id(category_id)
    
@category_routes.route("/update/<int:category_id>")
class UpdateCategory(Resource):
    @category_routes.expect(category_update_model)
    def patch(self, category_id):
        if not session.get("user_id"):
            return{
                "message": "Please login first"
            }, 401
        
        # if session.get("role") != "admin":
        #     return{
        #         "message": "Admin access required."
        #     }, 403
            
        data = category_update_model.parse_args()
        image = data.get("image")
        
        return update_category(category_id, data, image)
    
@category_routes.route("/status/<int:category_id>")
class UpdateCategoryStatus(Resource):
    @category_routes.expect(category_status_model)
    def patch(self, category_id):
        if not session.get("user_id"):
            return{
                "message": "Please login first."
            }, 401
            
        # if session.get("role") != "admin":
        #     return{
        #         "message": "Admin access required."
        #     }, 403
            
        data = category_routes.payload
        
        return update_category_status(category_id, data)
    
@category_routes.route("/delete/<int:category_id>")
class DeleteCategory(Resource):
    def delete(self, category_id):
        if not session.get("user_id"):
            return{
                "message": "Please login first"
            }, 401
            
        # if session.get("role") != "admin":
        #     return{
        #         "message": "Admin access required."
        #     }, 403
            
        return delete_category(category_id)