from flask import Flask, request, jsonify,Blueprint
from flask_cors import CORS
from supabase import create_client, Client


# Initialize Flask App
signin_bp = Blueprint('signin', __name__)
CORS(signin_bp)

# Supabase Credentials
SUPABASE_URL = "https://kchlbqeojqctvstmqeyi.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjaGxicWVvanFjdHZzdG1xZXlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMDEyNjMsImV4cCI6MjA1NTc3NzI2M30.91Q7YvObEJAlKzKN1C5kYNvgC-4NmMl_8syKQaKY0F0"

# Initialize Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Sign-in Route
@signin_bp.route("/signin", methods=["POST"])
def signin():
    try:
        data = request.json  
        email = data.get("email")
        password = data.get("password")  

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        print("\n----- Sign-in Request -----")
        print(f"Email: {email}")

        # Check if user exists
        user_response = supabase.table("users").select("*").eq("email", email).execute()
        doctor_response = supabase.table("doctors").select("*").eq("email", email).execute()

        if user_response.data:
            user = user_response.data[0]
            if user["password"] == password:  # ⚠️ Use hashed password verification in production
                return jsonify({"message": "User login successful!", "role": "user"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        elif doctor_response.data:
            doctor = doctor_response.data[0]
            if doctor["password"] == password:  # ⚠️ Use hashed password verification in production
                return jsonify({"message": "Doctor login successful!", "role": "doctor"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return jsonify({"error": str(e)}), 500


