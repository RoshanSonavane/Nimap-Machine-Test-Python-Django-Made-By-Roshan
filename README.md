# Nimap-Machine-Test-Python-Django-Made-By-Roshan
This is project submission for Nimap Infotech.


## Overview

This project is a Django-based REST API integrated with a PostgreSQL database. It provides endpoints for CRUD operations, and it is designed to be scalable, maintainable, and easy to extend.

## Features

- RESTful API endpoints
- PostgreSQL database integration
- Token-based authentication (e.g., JWT or Django's built-in authentication)
- Well-structured Django app with models, views, serializers, and routing
- Modular and scalable architecture

## Technologies Used

- **Django**: Backend framework
- **Django REST Framework (DRF)**: For creating the REST API
- **PostgreSQL**: Relational database
- **Authentication**: Token-based (JWT or session)

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django 4.x+
- PostgreSQL 13.x+
- Virtualenv (for managing virtual environments)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RoshanSonavane/Nimap.git
cd Nimap
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database

Update the `DATABASES` setting in your `settings.py` file with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/admin`.

## API Documentation

### Base URL

```plaintext
http://127.0.0.1:8000/app1/
```

### Example Endpoints

- **GET** `/app1/clients/`: Fetch all clients
- **POST** `/apo1/clients/`: Create a new item
- **PUT** `/app1/clients/{id}/`: Update an item by ID
- **DELETE** `/app1/clients/{id}/`: Delete an item by ID

- Same for Project Section

### Authentication

- Token-based authentication using JWT (or Django Sessions).
