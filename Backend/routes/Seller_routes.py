from flask_restx import Namespace, Resource, reqparse, fields
from flask import  request,session
from werkzeug.datastructures import FileStorage
from models.Sellers import Seller
from services.Sellers_services import create_seller, get_seller, update_seller, update_seller_status, delete_seller

seller_routes = Namespace("Seller API", description="Seller APIs")

Seller_model = reqparse.RequestParser()
Seller_model.add_argument(
    "shop_name",
    type=str,
    required=True,
    help="Shop name is required.",
    location="form"
)

Seller_model.add_argument(
    "shop_logo",
    type=FileStorage,
    required=False,
    help="Upload shop logo.",
    location="files"
)

Seller_model.add_argument(
    "shop_description",
    type=str,
    required=False,
    location="form"
)

Seller_model.add_argument(
    "shop_address",
    type=str,
    required=False,
    location="form"
)

# ========== seller update model ==========
seller_update_model = reqparse.RequestParser()

seller_update_model.add_argument(
    "shop_name",
    type=str,
    required=False,
    location = "form"
)

seller_update_model.add_argument(
    "shop_logo",
    type = FileStorage,
    required=False,
    location = "files",
    help="Upload new shop logo"
)

seller_update_model.add_argument(
    "shop_description",
    type = str,
    required = False,
    location = "form",
)

seller_update_model.add_argument(
    "shop_address",
    type = str,
    required = False,
    location = "form"
)

# ===== seller status mode =======
Seller_status_model = reqparse.RequestParser()
Seller_status_model.add_argument(
    "status",
    type = str,
    required = True,
    help="pending / approved / rejected / blocked",
    location = "form"
)

@seller_routes.route("/create")
class CreateSeller(Resource):
    @seller_routes.expect(Seller_model, validate=True)
    def post(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"message": "User not logged in."}, 401
        data = Seller_model.parse_args()
        
        shop_logo = data.get("shop_logo")
        return create_seller(data, user_id, shop_logo)


@seller_routes.route("/profile")
class SellerProfile(Resource):
    
    def get(self):
        user_id = session.get("user_id")
        
        if not user_id:
            return{
                "message": "Please login first"
            }, 401
            
        return get_seller(user_id)

@seller_routes.route("/update")
class UpdateSeller_Route(Resource):
    @seller_routes.expect(seller_update_model)
    def put(self):
        
        user_id = session.get("user_id")
        
        if not user_id:
            return{
                "message": "Please login first"
            }, 401
            
        data = seller_update_model.parse_args()
        
        shop_logo = data.get("shop_logo")
        
        
        return update_seller(user_id, data, shop_logo)

@seller_routes.route("/status/<int:seller_id>")
class UpdateSellerStatus(Resource):
    @seller_routes.expect(Seller_status_model)
    def put(self, seller_id):
        if session.get("role") != "admin":
            return {
                "message": "Admin access required"
            }, 403
            
        data = Seller_status_model.parse_args()
        
        return update_seller_status(
            seller_id,
            data
        )
        
@seller_routes.route("/delete/<int:seller_id>")
class DeleteSellerRoute(Resource):
    def delete(self, seller_id):
        
        user_id = session.get("user_id")
        role = session.get("role")
        
        if not user_id:
            return{
                "message": "Please login first"
            }, 401
            
        seller = Seller.query.get(seller_id)
            
        if not seller:
            return{
                "message": "Seller not found"
            }, 404
            
        if role == "admin":
            return delete_seller(seller_id)
        
        if role == "seller":
            if seller.user_id != user_id:
                return{
                    "message": "You can only delete your own seller profile"
                }, 403
                
            return delete_seller(seller_id)
        return {
            "message": "You are not allowed tp delete seller profiles"
        }, 403