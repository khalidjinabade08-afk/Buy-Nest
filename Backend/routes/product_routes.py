from flask import session
from flask_restx import Namespace, Resource, reqparse
from werkzeug.datastructures import FileStorage

from services.Product_service import create_product

product_routes = Namespace(
    "Product",
    description="Product Management"
)

product_parser = reqparse.RequestParser()
product_parser.add_argument(
    "name",
    type = str,
    required = True,
    location  = "form",
    help = "Product name is required"
)

product_parser.add_argument(
    "description",
    type = str,
    required = False,
    location = "form"
)

product_parser.add_argument(
    "price",
    type = float,
    required = True,
    location = "form",
    help = "Product price is required"
)

product_parser.add_argument(
    "quantity",
    type = int,
    required = True,
    location = "form",
    help = "Product quantity is required"
)

product_parser.add_argument(
    "category_id",
    type = int,
    required = True,
    location = "form",
    help = "Category ID is required"
)

product_parser.add_argument(
    "discount",
    type = int,
    required = False,
    default = 0,
    location = "form"
)

product_parser.add_argument(
    "discount_start",
    type = str,
    required = False,
    location = "form"
)

product_parser.add_argument(
    "discount_end",
    type = str,
    required = False,
    location = "form"
)

product_parser.add_argument(
    "image",
    type = FileStorage,
    required = True,
    location = "files",
    help = "Product image is required"
)

@product_routes.route("/create")
class CreateProduct(Resource):
    @product_routes.expect(product_parser)
    def post(self):
        user_id = session.get("user_id")
        
        if not user_id:
            return{
                "message": "Please login first"
            }, 401
        
        role = session.get("role")
        
        if role != "seller":
            return{
                "message": "Only seller can create product"
            }, 403
            
        data = product_parser.parse_args()
        
        image = data.pop("image")
        
        return create_product(data=data, user_id=user_id, image=image)