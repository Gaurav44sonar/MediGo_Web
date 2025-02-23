from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Initialize configurations
    app.config.from_pyfile('config.py')

    # Initialize extensions (e.g., database, authentication)
    # db.init_app(app)
    # login_manager.init_app(app)

    # Register Blueprints
    from .nearbyDoctors import nearByDoctors_bp
    from .doctor_User_SignUp import doctor_user_signup_bp
    from .user_SignIn import signin_bp
    app.register_blueprint(nearByDoctors_bp)
    app.register_blueprint(doctor_user_signup_bp)
    app.register_blueprint(signin_bp)
    return app
