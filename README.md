1.  Prerequisites
Before running the backend, ensure you have the following installed:

Python 3.8+
MongoDB (running locally or via MongoDB Atlas cloud service)
Pip package manager

2. Install Required Dependencies
Open a terminal and install the necessary libraries:
pip install fastapi uvicorn pymongo bcrypt

fastapi → API framework
uvicorn → ASGI server for running FastAPI
pymongo → MongoDB driver for Python
bcrypt → Secure password hashing

3. Configure and Start MongoDB
If using local MongoDB, start the server:
mongod --dbpath /path/to/mongodb/data

If using MongoDB Atlas (Cloud Service), update the connection string in backend.py:
client = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net/trustlocal")

4. Run the FastAPI Backend
Start the FastAPI server using Uvicorn:
uvicorn backend:app --reload

The --reload flag enables hot reloading during development.

The API will now be accessible at http://127.0.0.1:8000.

5. API Endpoints & Usage
User Authentication
Register a new user

Endpoint: POST /register
Request Body:
json
Copy
Edit
{
  "username": "user123",
  "password": "securepassword"
}
Response:
json
Copy
Edit
{ "message": "User registered successfully" }
Login a user

Endpoint: POST /login
Response:
json
Copy
Edit
{ "message": "Login successful" }
🏢 Business Listings
Add a new business

Endpoint: POST /businesses
Request Body:
json
Copy
Edit
{
  "name": "Local Coffee Shop",
  "category": "Cafe",
  "location": "Downtown",
  "owner": "John Doe"
}
Response:
json
Copy
Edit
{ "message": "Business added successfully" }
Retrieve all businesses

Endpoint: GET /businesses
Response Example:
json
Copy
Edit
[
  {
    "name": "Local Coffee Shop",
    "category": "Cafe",
    "location": "Downtown",
    "owner": "John Doe"
  }
]

6. Review System
Add a review for a business

Endpoint: POST /reviews
Request Body:
json
Copy
Edit
{
  "business_id": "Local Coffee Shop",
  "username": "user123",
  "rating": 5,
  "comment": "Great place with amazing coffee!"
}
Response:
json
Copy
Edit
{ "message": "Review added successfully" }
Retrieve reviews for a business

Endpoint: GET /reviews/{business_id}
Example Request: GET /reviews/Local%20Coffee%20Shop
Response Example:
json
Copy
Edit
[
  {
    "business_id": "Local Coffee Shop",
    "username": "user123",
    "rating": 5,
    "comment": "Great place with amazing coffee!"
  }
