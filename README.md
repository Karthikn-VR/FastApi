# FastAPI User Management API

## Overview

A simple backend application built with FastAPI that provides basic CRUD operations for managing users.
The project demonstrates API design, request validation, database integration, and frontend-backend interaction.

---

## Tech Stack

* Backend: FastAPI
* Database: SQLite
* ORM: SQLAlchemy
* Validation: Pydantic
* Server: Uvicorn
* Frontend: HTML, CSS, JavaScript (Fetch API)

---

## Features

* Create user
* Get all users
* Get user by ID
* Delete user
* Input validation
* Error handling
* RESTful API design

---

## Project Structure

```
app/
 ├── main.py
 ├── database.py
 ├── models.py
 ├── schemas.py
frontend/
 └── index.html
```

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/Karthikn-VR/FastApi.git
cd FastApi
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Interactive docs:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Create User

```
POST /users
```

### Get All Users

```
GET /users
```

### Get User by ID

```
GET /users/{id}
```

### Delete User

```
DELETE /users/{id}
```

---

## Notes

* Database file (`test.db`) is not included in the repository.
* `.gitignore` excludes environment files and cache.
* This project uses in-memory + SQLite for learning purposes.

---

## Future Improvements

* Add update (PUT/PATCH) functionality
* Implement authentication (JWT)
* Add pagination and filtering
* Migrate to PostgreSQL
* Convert frontend to React

---

## Author

Karthik
