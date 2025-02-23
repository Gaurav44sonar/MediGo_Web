
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from supabase import create_client
# from geopy.distance import geodesic  # To calculate distance

# def nearByDoctors():
#     print("I am from doctors")
#     app = Flask(__name__)
#     CORS(app)  # Enable CORS to allow frontend access

#     # ✅ Supabase Credentials
#     SUPABASE_URL = "https://kchlbqeojqctvstmqeyi.supabase.co"
#     SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjaGxicWVvanFjdHZzdG1xZXlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMDEyNjMsImV4cCI6MjA1NTc3NzI2M30.91Q7YvObEJAlKzKN1C5kYNvgC-4NmMl_8syKQaKY0F0"

#     # ✅ Supabase Client
#     supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

#     @app.route("/doctors", methods=["GET"])
#     def get_doctors():
#         try:
#             user_lat = request.args.get("latitude", type=float)
#             user_lon = request.args.get("longitude", type=float)
#             if user_lat is None or user_lon is None:
#                 return jsonify({"error": "Missing latitude or longitude"}), 400
            
#             # ✅ Fetch doctors from Supabase
#             response = supabase_client.table("doctors").select("*").execute()

#             if response.data:
#                 doctor_list = []

#                 for doctor in response.data:
#                     doctor_location = (doctor["latitude"], doctor["longitude"])
#                     user_location = (user_lat, user_lon)

#                     # ✅ Calculate distance
#                     distance_km = round(geodesic(user_location, doctor_location).km, 2)

#                     # ✅ Filter doctors within 50km
#                     if distance_km <= 50:
#                         doctor_data = {
#                             "name": doctor["name"],
#                             "specialty": doctor["specialty"],
#                             "hospital_name": doctor["hospital_name"],
#                             "location": doctor["location"],
#                             "fees": doctor["fees"],
#                             "rating": doctor["rating"],
#                             "distance": distance_km,
#                             "image_url": doctor['image_url']
#                         }
#                         doctor_list.append(doctor_data)

#                 # ✅ Sort by distance
#                 doctor_list.sort(key=lambda x: x["distance"])

#                 return jsonify(doctor_list)

#             else:
#                 return jsonify({"message": "No doctors found"}), 404

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

#     return app  # ✅ Return the app instead of running it directly

# models/nearbyDoctors.py
from flask import Blueprint, jsonify, request
from flask_cors import CORS
from supabase import create_client
from geopy.distance import geodesic

# Initialize Supabase Client
SUPABASE_URL = "https://kchlbqeojqctvstmqeyi.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjaGxicWVvanFjdHZzdG1xZXlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMDEyNjMsImV4cCI6MjA1NTc3NzI2M30.91Q7YvObEJAlKzKN1C5kYNvgC-4NmMl_8syKQaKY0F0"

supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create Blueprint
nearByDoctors_bp = Blueprint('nearByDoctors', __name__)
CORS(nearByDoctors_bp)  # Enable CORS for this blueprint

@nearByDoctors_bp.route('/doctors', methods=['GET'])
def get_doctors():
    try:
        user_lat = request.args.get("latitude", type=float)
        user_lon = request.args.get("longitude", type=float)
        if user_lat is None or user_lon is None:
            return jsonify({"error": "Missing latitude or longitude"}), 400

        # Fetch doctors from Supabase
        response = supabase_client.table("doctors").select("*").execute()

        if response.data:
            doctor_list = []
            for doctor in response.data:
                doctor_location = (doctor["latitude"], doctor["longitude"])
                user_location = (user_lat, user_lon)
                distance_km = round(geodesic(user_location, doctor_location).km, 2)
                if distance_km <= 50:
                    doctor_data = {
                        "name": doctor["name"],
                        "specialty": doctor["specialty"],
                        "hospital_name": doctor["hospital_name"],
                        "location": doctor["location"],
                        "fees": doctor["fees"],
                        "rating": doctor["rating"],
                        "distance": distance_km,
                        "image_url": doctor['image_url']
                    }
                    doctor_list.append(doctor_data)
            doctor_list.sort(key=lambda x: x["distance"])
            return jsonify(doctor_list)
        else:
            return jsonify({"message": "No doctors found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

