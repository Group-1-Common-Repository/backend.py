# TrustLocal - Backend Setup (`backend.py`)

This **FastAPI backend** powers the **TrustLocal: Local Business Directory and Review System**, handling **user authentication, business listings, and reviews** while storing data in **MongoDB**.

---

## Prerequisites
Before running the backend, ensure you have the following installed:

- **Python 3.8+**
- **MongoDB (running locally or via MongoDB Atlas cloud service)**
- **Pip package manager**

---

## Install Required Dependencies
Open a terminal and install the necessary Python libraries:

```sh
pip install fastapi uvicorn pymongo bcrypt
```

- `fastapi` → API framework  
- `uvicorn` → ASGI server for running FastAPI  
- `pymongo` → MongoDB driver for Python  
- `bcrypt` → Secure password hashing  

---

## Configure and Start MongoDB
- If using **local MongoDB**, start the server:

  ```sh
  mongod --dbpath /path/to/mongodb/data
  ```

- If using **MongoDB Atlas (Cloud Service)**, update the connection string in `backend.py`:

  ```python
  client = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net/trustlocal")
  ```

---

## Run the FastAPI Backend
Start the FastAPI server using **Uvicorn**:

```sh
uvicorn backend:app --reload
```

- The **`--reload` flag** enables **hot reloading** during development.  
- The API will now be accessible at **`http://127.0.0.1:8000`**.  

---

## API Endpoints & Usage

### User Authentication
- **Register a new user**  
  - **Endpoint:** `POST /register`  
  - **Request Body:**  
    ```json
    {
      "username": "user123",
      "password": "securepassword"
    }
    ```
  - **Response:**  
    ```json
    { "message": "User registered successfully" }
    ```

- **Login a user**  
  - **Endpoint:** `POST /login`  
  - **Response:**  
    ```json
    { "message": "Login successful" }
    ```

---

### Business Listings
- **Add a new business**  
  - **Endpoint:** `POST /businesses`  
  - **Request Body:**  
    ```json
    {
      "name": "Local Coffee Shop",
      "category": "Cafe",
      "location": "Downtown",
      "owner": "John Doe"
    }
    ```
  - **Response:**  
    ```json
    { "message": "Business added successfully" }
    ```

- **Retrieve all businesses**  
  - **Endpoint:** `GET /businesses`  
  - **Response Example:**  
    ```json
    [
      {
        "name": "Local Coffee Shop",
        "category": "Cafe",
        "location": "Downtown",
        "owner": "John Doe"
      }
    ]
    ```

---

### Review System
- **Add a review for a business**  
  - **Endpoint:** `POST /reviews`  
  - **Request Body:**  
    ```json
    {
      "business_id": "Local Coffee Shop",
      "username": "user123",
      "rating": 5,
      "comment": "Great place with amazing coffee!"
    }
    ```
  - **Response:**  
    ```json
    { "message": "Review added successfully" }
    ```

- **Retrieve reviews for a business**  
  - **Endpoint:** `GET /reviews/{business_id}`  
  - **Example Request:** `GET /reviews/Local%20Coffee%20Shop`  
  - **Response Example:**  
    ```json
    [
      {
        "business_id": "Local Coffee Shop",
        "username": "user123",
        "rating": 5,
        "comment": "Great place with amazing coffee!"
      }
    ]
    ```

