# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
# from supabase import create_client, Client
# import requests

# # Initialize Flask App
# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend interaction

# # Supabase Credentials
# SUPABASE_URL = "https://kchlbqeojqctvstmqeyi.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjaGxicWVvanFjdHZzdG1xZXlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMDEyNjMsImV4cCI6MjA1NTc3NzI2M30.91Q7YvObEJAlKzKN1C5kYNvgC-4NmMl_8syKQaKY0F0"


# # Initialize Supabase Client
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# # Signup Route
# @app.route("/signup", methods=["POST"])
# def signup():
#     try:
#         # Get Common Fields
#         name = request.form.get("name")
#         email = request.form.get("email")
#         password = request.form.get("password")  # Normally should be hashed
#         mobile = request.form.get("mobile")
#         role = request.form.get("role")  # "doctor" or "user"

#         # Print received data
#         print("\n----- New Signup Request -----")
#         print(f"Name: {name}")
#         print(f"Email: {email}")
#         print(f"Password: {password}")  # ⚠️ Should not be printed in production
#         print(f"Mobile: {mobile}")
#         print(f"Role: {role}")

#         # Insert User Data into Supabase
#         if role == "user":
#             response = supabase.table("users").insert({
#                 "name": name,
#                 "email": email,
#                 "password": password,  # ⚠️ Ideally, hash this before storing
#                 "mobile": mobile,
#             }).execute()

#             print("📌 User data stored in Supabase!")
#             return jsonify({"message": "User signup successful!"}), 200

#         # Insert Doctor Data into Supabase
#         elif role == "doctor":
#             specialty = request.form.get("specialty")
#             hospital = request.form.get("hospital")
#             location = request.form.get("location")
#             license = request.files.get("license")  # File Upload

#             print(f"Specialty: {specialty}")
#             print(f"Hospital: {hospital}")
#             print(f"Location: {location}")

#             # lati,longi=get_coordinates(location)

#             # print("Latitude: ",lati)
#             # print("Longitude: ",longi)

#             # Handle File Upload
    
#             # Store Doctor Data in Supabase
#             response = supabase.table("doctors").insert({
#                 "name": name,
#                 "email": email,
#                 "password": password,  # ⚠️ Ideally, hash this before storing
#                 "mobile": mobile,
#                 "specialty": specialty,
#                 "hospital_name": hospital,
#                 "location": location,
#                  "latitude":4,
#                  "longitude":4
#             }).execute()

#             print("📌 Doctor data stored in Supabase!")
#             return jsonify({"message": "Doctor signup successful!"}), 200

#         return jsonify({"error": "Invalid role"}), 400

#     except Exception as e:
#         print(f"⚠️ Error: {e}")
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Blueprint, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

doctor_user_signup_bp = Blueprint('doctor_user_signup', __name__)
CORS(doctor_user_signup_bp)  # Enable CORS for this blueprint

# Supabase Credentials
SUPABASE_URL = "https://kchlbqeojqctvstmqeyi.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjaGxicWVvanFjdHZzdG1xZXlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMDEyNjMsImV4cCI6MjA1NTc3NzI2M30.91Q7YvObEJAlKzKN1C5kYNvgC-4NmMl_8syKQaKY0F0"

# Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@doctor_user_signup_bp.route("/signup", methods=["POST"])
def signup():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        mobile = request.form.get("mobile")
        role = request.form.get("role")

        if role == "user":
            response = supabase.table("users").insert({
                "name": name,
                "email": email,
                "password": password,
                "mobile": mobile,
            }).execute()
            return jsonify({"message": "User signup successful!"}), 200
        elif role == "doctor":
            specialty = request.form.get("specialty")
            hospital = request.form.get("hospital")
            location = request.form.get("location")
            license = request.files.get("license")
            response = supabase.table("doctors").insert({
                "name": name,
                "email": email,
                "password": password,
                "mobile": mobile,
                "specialty": specialty,
                "hospital_name": hospital,
                "location": location,
                "latitude": 4,  # Placeholder value
                "longitude": 4  # Placeholder value
            }).execute()
            return jsonify({"message": "Doctor signup successful!"}), 200
        else:
            return jsonify({"error": "Invalid role"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

