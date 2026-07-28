from models.user import User
from models.OTP import OTP
from database.db import db
from werkzeug.security import generate_password_hash
from utils.response import success_response, error_response

def VerifyOTP(data):
    try:
        email = data.get("email")
        otp = data.get("OTP")
    except Exception as e:
        db.session.rollback()
        return error_response(str(e),200)