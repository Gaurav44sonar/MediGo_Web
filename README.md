# MediGo_Web
MediGo: Instant Doctor Consultation &amp; Booking
## Table of Contents
1. [Introduction](#Introduction)
2. [Features](#Features)
3. [Installation and Setup](#Installation_and_Setup)
4. [Technologies Used](#Technologies_Used)
5. [Usage Guide](#Usage_Guide)
6. [Future Enhancements](#Future_Enhacements)
7. [Contributers](#contributers)
---

## Introduction

*MediGo* is a web application designed for quick and efficient doctor appointments, with a strong focus on emergency situations. It allows users to search for doctors based on location, schedule appointments, and manage patient records. 


## 2. Features  

### *User Side*  
✅ *Signup/Login:* Separate registration for users and doctors.  
✅ *Home Page:* Includes a "Find Doctor" feature for quick access.  
✅ *Find Doctor Page:*  
   - Location-based search to find nearby doctors.  
   - Displays doctor profiles with details.  
✅ *Emergency Assistance:*  
   - Users can search for doctors near their location in emergencies.  
✅ *Appointment Booking:*  
   - Users can book appointments with doctors.  

### *Doctor Side*  
✅ *Dashboard:* Manage appointments, view schedules.  
✅ *Patient File Management:* Store and access patient medical records.  
✅ *Appointment Management:* Accept, reschedule, or cancel appointments. 

## 3. Installation & Setup  

### *Prerequisites*  
- Node.js  
- MongoDB (or any preferred database)  
- Express.js  
- React.js (Frontend)  
- Postman (For API testing, optional)  

### *Steps to Run the Application*  
1. *Clone the Repository*  
   bash
   git clone https://github.com/your-repository/medigo.git
   cd medigo
   

2. *Install Dependencies*  
   - Backend  
     bash
     cd server
     npm install
       
   - Frontend  
     bash
     cd client
     npm install
       

3. *Setup Environment Variables*  
   - Create a .env file in the backend directory with:  
     
     PORT=5000
     MONGO_URI=your-mongodb-uri
     JWT_SECRET=your-secret-key
       

4. *Run the Application*  
   - Backend:  
     bash
     npm run server
       
   - Frontend:  
     bash
     npm start
       

## 4. Technologies Used  
- *Frontend:* HTML,CSS,JavaScript  
- *Backend:* Python,Flask
- *Database:* Supabase

## 5. Usage Guide  

### *User Flow*  
1. *Sign Up/Login*  
2. *Search for a Doctor*  
3. *Book an Appointment*  
4. *Receive Confirmation*  

### *Doctor Flow*  
1. *Sign Up/Login*  
2. *Manage Appointments*  
3. *Access Patient Records*  
4. *Update Availability*

## 8. Future Enhancements  
🔹 *Live Chat with Doctors*  
🔹 *AI-based Doctor Recommendations*  
🔹 *Payment Integration for Online Consultation*  

## 9. Contributors  
- *Gaurav Sonar* – Group Leader : Backend Developer
- *Nitin Panzade* - Member : Frontend Developer
- *Purva Thakare* - Member : Frontend Developer
- *Sneha Phase* - Member : Designer



