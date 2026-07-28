from flask_restx import Namespace, Resource, fields
from flask import request
from services.user_services import Register, VerifyOTPService

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