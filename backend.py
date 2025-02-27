from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
import bcrypt

# Initialize FastAPI
app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["trustlocal"]
users_collection = db["users"]
businesses_collection = db["businesses"]
reviews_collection = db["reviews"]

# User model
class User(BaseModel):
    username: str
    password: str

# Business model
class Business(BaseModel):
    name: str
    category: str
    location: str
    owner: str

# Review model
class Review(BaseModel):
    business_id: str
    username: str
    rating: int
    comment: str

# Hash password function
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

# Verify password function
def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

# User Registration
@app.post("/register")
def register(user: User):
    if users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = hash_password(user.password)
    users_collection.insert_one({"username": user.username, "password": hashed_password})
    return {"message": "User registered successfully"}

# User Login
@app.post("/login")
def login(user: User):
    db_user = users_collection.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful"}

# Add a Business
@app.post("/businesses")
def add_business(business: Business):
    businesses_collection.insert_one(business.dict())
    return {"message": "Business added successfully"}

# Get all Businesses
@app.get("/businesses")
def get_businesses():
    return list(businesses_collection.find({}, {"_id": 0}))

# Add a Review
@app.post("/reviews")
def add_review(review: Review):
    if not businesses_collection.find_one({"name": review.business_id}):
        raise HTTPException(status_code=404, detail="Business not found")
    
    reviews_collection.insert_one(review.dict())
    return {"message": "Review added successfully"}

# Get Reviews for a Business
@app.get("/reviews/{business_id}")
def get_reviews(business_id: str):
    return list(reviews_collection.find({"business_id": business_id}, {"_id": 0}))
