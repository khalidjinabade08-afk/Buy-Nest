from flask_restx import Namespace, Resource, fields
from flask import request, session, Flask
from services.user_services import Register, VerifyOTPService, loging, DeleteUser, Show_all, profile

auth_routes = Namespace("Admin API", description="Authentication APIs")

# ----------------- SWAGGER MODELS -----------------

register_model = auth_routes.model(
    "Register",
    {
        "name": fields.String(required=True, description="name"),
        "email": fields.String(required=True, description="email"),
        "password": fields.String(required=True, description="password"),
        "role": fields.String(required=True, description="admin/customer")   
    },
)
verify_otp_model = auth_routes.model(
    "VerifyOTP",
    {
        "email": fields.String(required=True, description="Registered email"),
        "otp": fields.String(required=True, description="6-digit OTP code")
    },
)

loging_model = auth_routes.model(
    "Login",
    {
        "email": fields.String(required=True, description="Registered email"),
        "password": fields.String(required=True, description="Password")
    },
)

# ----------------- ROUTES -----------------

# Register Route
@auth_routes.route("/register")
class register(Resource):
    @auth_routes.expect(register_model, validate=True)
    def post(self):
        data = request.get_json()
        return Register(data)

# Verify OTP Route
@auth_routes.route("/verify-otp")
class verify_otp(Resource):
    @auth_routes.expect(verify_otp_model, validate=True)
    def post(self):
        data = request.get_json()
        return VerifyOTPService(data)

# Loging Route
@auth_routes.route("/loging")
class UserLoging(Resource):
    @auth_routes.expect(loging_model, validate=True)
    def post(self):
        data = request.get_json()
        return loging(data)
    
# Delete Route
@auth_routes.route("/delete/<int:user_id>")
class deleteUser(Resource):
    def delete(self, user_id):
        return DeleteUser(user_id)
    
# Show all Route
@auth_routes.route("/Users") 
class AllUsersList(Resource):
    def get(self):
        user_id = session.get("user_id")
        if not user_id:
            return {"status": "error", "message": "Unauthorized. Please log in first."}, 401
        return Show_all(user_id)
   
# show profile Route
@auth_routes.route("/find/<int:user_id>")
class GetUserById(Resource):
    def get(self, user_id):
        return profile(user_id) 