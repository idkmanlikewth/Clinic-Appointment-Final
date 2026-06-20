# Clinic Appointment Booking System

A secure and scalable Clinic Appointment Booking System built with **FastAPI**, **SQLAlchemy**, **PostgreSQL**, and **JWT Authentication**.

The system enables patients and doctors to register, authenticate securely, and manage appointments through RESTful APIs. JWT-based authentication ensures protected access to appointment-related operations.

> **Database note:** The app uses PostgreSQL by default in production and falls back to a local SQLite file only when no `DATABASE_URL` is configured. This matters because most hosting platforms (Render, Railway, Heroku, Fly.io, etc.) use an ephemeral filesystem — anything written to a SQLite file is wiped on every restart or redeploy. A managed Postgres database persists your data across deploys. See [Database Configuration](#database-configuration) below.

---

## Overview

This project demonstrates the implementation of a modern backend application using FastAPI. It follows REST API principles and incorporates authentication, database management, and CRUD operations.

### Key Capabilities

* Secure User Registration and Authentication
* Doctor Registration and Authentication
* JWT-Based Authorization
* Appointment Booking Management
* Appointment Cancellation
* Database Persistence using PostgreSQL (SQLite fallback for local dev)
* Interactive API Documentation

---

## System Architecture

```text
Client (Postman / Swagger UI)
            │
            ▼
        FastAPI
            │
            ▼
     Authentication
      (JWT Tokens)
            │
            ▼
       SQLAlchemy
            │
            ▼
        PostgreSQL
```

---

## Features

### Patient Management

* Register a new patient account
* Secure login using JWT authentication
* View personal appointments

### Doctor Management

* Register doctor profiles
* Secure doctor authentication
* Manage specialization details

### Appointment Management

* Schedule appointments with doctors
* View booked appointments
* Cancel existing appointments

### Security

* Password hashing using BCrypt
* JWT Access Tokens
* Protected API endpoints
* Token-based authorization

---

## Technology Stack

| Component         | Technology       |
| ----------------- | ---------------- |
| Backend Framework | FastAPI          |
| Database          | PostgreSQL (SQLite fallback for local dev) |
| ORM               | SQLAlchemy       |
| Authentication    | JWT              |
| Password Hashing  | Passlib (BCrypt) |
| API Testing       | Postman          |
| Documentation     | Swagger UI       |

---

## Project Structure

```text
clinic_management/
│
├── auth.py
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── clinic.db          # only created/used if DATABASE_URL is unset
├── .env                # not committed -- create from .env.example
├── .env.example
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<username>/clinic-appointment-booking-system.git

cd clinic-appointment-booking-system
```

### Create Virtual Environment

```bash
python -m venv clinic_management
```

### Activate Virtual Environment

**Windows**

```bash
clinic_management\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

The app reads its database connection string from the `DATABASE_URL` environment variable.

* **If `DATABASE_URL` is set** → it connects to that PostgreSQL database.
* **If `DATABASE_URL` is not set** → it falls back to a local SQLite file (`clinic.db`) so you can still run the project with zero setup. This is fine for quick local testing, but **do not rely on it in production/deployed environments** — SQLite's file is stored on local disk, and most hosting platforms (Render, Railway, Heroku, Fly.io, etc.) reset the filesystem on every restart or redeploy, silently wiping all your data.

### 1. Get a Postgres database

Use any provider you like, for example:

* [Render](https://render.com) (free Postgres instances)
* [Railway](https://railway.app)
* [Supabase](https://supabase.com)
* [Neon](https://neon.tech)
* A local Postgres install (`postgresql://postgres:postgres@localhost:5432/clinic_db`)

### 2. Configure the connection string

Copy the example env file and fill in your real connection string:

```bash
cp .env.example .env
```

Edit `.env`:

```text
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database_name>
```

If your provider gives you a URL starting with `postgres://` (Heroku-style), that's fine too — the app automatically normalizes it to `postgresql://` for SQLAlchemy.

### 3. Set the same variable on your deployment platform

Whatever platform you deploy to (Render, Railway, Fly.io, etc.), add `DATABASE_URL` as an environment variable in its dashboard/settings, using the same connection string. The app will pick it up automatically on startup — no code changes needed.

Tables are created automatically on startup via `Base.metadata.create_all(bind=engine)` in `main.py`, so the first time the app connects to a fresh Postgres database, it will create the `users`, `doctors`, and `appointments` tables for you.

---

## Running the Application

Start the FastAPI development server:

```bash
fastapi dev main.py
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## Authentication Workflow

1. Register a User or Doctor account
2. Log in using valid credentials
3. Receive a JWT Access Token
4. Include the token in the Authorization header

Example:

```text
Authorization: Bearer <access_token>
```

Protected endpoints require a valid JWT token.

---

## API Endpoints

### User APIs

| Method | Endpoint       | Description         |
| ------ | -------------- | ------------------- |
| POST   | `/user/signup` | Register a new user |
| POST   | `/user/login`  | Authenticate user   |

### Doctor APIs

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | `/doctor/signup` | Register a doctor   |
| POST   | `/doctor/login`  | Authenticate doctor |

### Appointment APIs

| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| POST   | `/appointments/book` | Book an appointment   |
| GET    | `/appointments/my`   | Retrieve appointments |
| DELETE | `/appointments/{id}` | Cancel appointment    |

---

## Sample Workflow

```text
User Registration
        │
        ▼
User Login
        │
        ▼
Receive JWT Token
        │
        ▼
Doctor Registration
        │
        ▼
Book Appointment
        │
        ▼
View Appointments
        │
        ▼
Cancel Appointment
```

---

## Testing

The APIs can be tested using:

* Postman
* Swagger UI
* FastAPI Interactive Documentation

---

## Learning Objectives

This project demonstrates:

* RESTful API Design
* JWT Authentication and Authorization
* Database Integration with SQLAlchemy
* CRUD Operations
* Secure Password Management
* FastAPI Development
* API Documentation and Testing

---

## License

This project is intended for educational and academic purposes.
