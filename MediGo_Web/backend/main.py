# from models.nearbyDoctors import nearByDoctors  # ✅ Import the function



# app = nearByDoctors()  # ✅ Create the Flask app

# print("i am from main")
# if __name__ == "__main__":
#     app.run(debug=True)  # ✅ Run the app from main.py


from flask import Flask
from app.nearbyDoctors import nearByDoctors_bp
from app.doctor_User_SignUp import doctor_user_signup_bp
from app.user_SignIn import signin_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(nearByDoctors_bp)
    app.register_blueprint(doctor_user_signup_bp)
    app.register_blueprint(signin_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
