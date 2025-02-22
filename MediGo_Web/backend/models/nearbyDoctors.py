# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from supabase import create_client
# from geopy.distance import geodesic  # To calculate distance

# app = Flask(__name__)
# CORS(app)  # Enable CORS to allow frontend access

# # ✅ Correct Supabase Credentials
# SUPABASE_URL = "https://kchlbqeojqctvstmqeyi.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjaGxicWVvanFjdHZzdG1xZXlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMDEyNjMsImV4cCI6MjA1NTc3NzI2M30.91Q7YvObEJAlKzKN1C5kYNvgC-4NmMl_8syKQaKY0F0"

# # ✅ Correct Supabase Client
# supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

# @app.route("/doctors", methods=["GET"])
# def get_doctors():
#     try:
#         # ✅ Check if latitude & longitude are provided
#         user_lat = request.args.get("latitude", type=float)
#         user_lon = request.args.get("longitude", type=float)
#         if user_lat is None or user_lon is None:
#             return jsonify({"error": "Missing latitude or longitude"}), 400
        
#         # ✅ Fetch doctors from Supabase
#         response = supabase_client.table("doctors").select("*").execute()

#         # ✅ Ensure data is returned
#         if response.data:
#             doctor_list = []

#             for doctor in response.data:
#                 doctor_location = (doctor["latitude"], doctor["longitude"])
#                 user_location = (user_lat, user_lon)

#                 # ✅ Calculate distance using geopy
#                 distance_km = round(geodesic(user_location, doctor_location).km, 2)

#                 # ✅ Append doctor info with calculated distance
#                 doctor["distance"] = distance_km
#                 doctor_list.append(doctor)

#             # ✅ Sort doctors by distance
#             doctor_list.sort(key=lambda x: x["distance"])

#             return jsonify(doctor_list)

#         else:
#             return jsonify({"message": "No doctors found"}), 404

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client
from geopy.distance import geodesic  # To calculate distance

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend access

# ✅ Correct Supabase Credentials
SUPABASE_URL = "https://kchlbqeojqctvstmqeyi.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjaGxicWVvanFjdHZzdG1xZXlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMDEyNjMsImV4cCI6MjA1NTc3NzI2M30.91Q7YvObEJAlKzKN1C5kYNvgC-4NmMl_8syKQaKY0F0"

# ✅ Correct Supabase Client
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/doctors", methods=["GET"])
def get_doctors():
    try:
        # ✅ Check if latitude & longitude are provided
        user_lat = request.args.get("latitude", type=float)
        user_lon = request.args.get("longitude", type=float)
        if user_lat is None or user_lon is None:
            return jsonify({"error": "Missing latitude or longitude"}), 400
        
        # ✅ Fetch doctors from Supabase
        response = supabase_client.table("doctors").select("*").execute()

        # ✅ Ensure data is returned
        if response.data:
            doctor_list = []

            for doctor in response.data:
                doctor_location = (doctor["latitude"], doctor["longitude"])
                user_location = (user_lat, user_lon)

                # ✅ Calculate distance using geopy
                distance_km = round(geodesic(user_location, doctor_location).km, 2)

                # ✅ Append doctor info with calculated distance
                doctor["distance"] = distance_km
                doctor_list.append(doctor)

            # ✅ Sort doctors by distance
            doctor_list.sort(key=lambda x: x["distance"])

            return jsonify(doctor_list)

        else:
            return jsonify({"message": "No doctors found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
