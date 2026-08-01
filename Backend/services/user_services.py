from flask import session
from werkzeug.security import generate_password_hash, check_password_hash

from database.db import db
from models.user import User
from models.OTP import OTP
from utils.otp import generate_otp
from utils.email import send_otp_email
from utils.response import success_response, error_response


def Register(data):
    try:
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        if not all([name, email, password, role]):
            return error_response("All fields are required.", 400)

        name = name.lower()
        email = email.lower()

        if User.query.filter_by(name=name).first():
            return error_response("Name already exists.", 400)

        if User.query.filter_by(email=email).first():
            return error_response("Email already exists.", 400)

        if role not in ["seller", "customer"]:
            return error_response("Invalid role.", 400)

        otp = generate_otp()

        old_otp = OTP.query.filter_by(email=email).first()
        if old_otp:
            db.session.delete(old_otp)
            db.session.commit()

        otp_data = OTP(
            name=name,
            email=email,
            password=generate_password_hash(password),
            role=role,
            otp=str(otp)
        )

        db.session.add(otp_data)
        db.session.commit()

        send_otp_email(email, otp)

        return success_response(
            "OTP sent successfully.",
            {"email": email},
            200
        )

    except Exception as e:
        db.session.rollback()
        return error_response(str(e), 500)


def VerifyOTPService(data):
    try:
        email = data.get("email")
        submitted_otp = data.get("otp")

        if not email or not submitted_otp:
            return error_response("Email and OTP are required.", 400)

        email = email.lower()
        submitted_otp = str(submitted_otp).strip()

        otp_record = OTP.query.filter_by(email=email, otp=submitted_otp).first()

        if not otp_record:
            return error_response("Invalid OTP or Email.", 400)

        if User.query.filter_by(email=email).first():
            return error_response("User already exists.", 400)

        new_user = User(
            name=otp_record.name,
            email=otp_record.email,
            password=otp_record.password, 
            role=otp_record.role
        )

        db.session.add(new_user)
        db.session.delete(otp_record)
        db.session.commit()

        return success_response(
            "Registration successful! User verified and created.",
            {"email": new_user.email, "role": new_user.role},
            201
        )

    except Exception as e:
        db.session.rollback()
        return error_response(str(e), 500)


def loging(data):
    try:
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return error_response("Email and password are required.", 400)

        email = email.lower()

        currect_user = User.query.filter_by(email=email).first()

        if not currect_user:
            return error_response("Email not found.", 400)

        if not check_password_hash(currect_user.password, password):
            return error_response("Invalid Password.", 401)

        session["user_id"] = currect_user.id
        session["role"] = currect_user.role

        return success_response(
            "Login Successful",
            {
                "id": currect_user.id,
                "name": currect_user.name,
                "role": currect_user.role
            },
            200
        )

    except Exception as e:
        db.session.rollback()
        return error_response(str(e), 500)
    
def DeleteUser(user_id):
    try:
        current_user = User.query.get(user_id)
        
        if not current_user:
            return error_response("User not found")
        
        db.session.delete(current_user)
        db.session.commit()
        return success_response("User deleted", 404)
    
    except Exception as e:
        db.session.rollback()
        return error_response(str(e))
    
def Show_all(user_id):
    try:
        current_id = User.query.get(user_id)
        
        if not current_id:
            return error_response("User id not Found")
        
        all_users = User.query.all()
        
        user_list = []
        for user in all_users:
            user_list.append({
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role,
            })
            
        return success_response(
            "All users fetched successfully",
            user_list
        )
        
    except Exception as e:
        return error_response(str(e), 500)
    
def profile(user_id):
    try:
        target_user = User.query.get(user_id)
        
        if not target_user:
            return error_response("User not found.", 404)
            
        return success_response(
            "User found successfully.",
            {
                "id": target_user.id,
                "name": target_user.name,
                "email": target_user.email,
                "role": target_user.role
            },
            200
        )
    except Exception as e:
        return error_response(str(e))