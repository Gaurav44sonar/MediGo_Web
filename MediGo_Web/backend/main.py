from models.nearbyDoctors import nearByDoctors  # ✅ Import the function

app = nearByDoctors()  # ✅ Create the Flask app
print("i am from main")
if __name__ == "__main__":
    app.run(debug=True)  # ✅ Run the app from main.py
