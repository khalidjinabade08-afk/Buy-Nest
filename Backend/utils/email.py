from flask_mail import Message
from extensions import mail

def send_otp_email(email, otp):
    msg = Message(
        subject="OTP Verification",
        recipients=[email]
    )
    
    msg.body = f"""OTP Verification: To ensure secure registration, a One-Time Passsword {otp} is send to the user`s registered email address or mobile number. The user must enter the correct OTP to verify their identity. Upon successful OTP verification, the registration process is completed successfully."""
    mail.send(msg)