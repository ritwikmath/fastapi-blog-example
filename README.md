# FastAPI Project for Blog

This project is created to be used as an example in a Blog Post

# Prerequisite

1. Python 3.10 or above
2. PostgreSQL database server
3. Pgadmin or Dbeaver

# Project Setup

1. Create a databse named `postgres`
2. Create table `blogs`
```sql
CREATE TABLE blogs (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    description TEXT NOT NULL,
    created_by VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL DEFAULT NULL
);
```
3. Create file `.env` in root directory. Change the values as per your PostgreSQL database
```text
DB_HOST=localhost
DB_USER=postgres
DB_PASS=secret
DB_DATABASE=postgres
DB_PORT=5431
```
4. Install virtual environment
```bash
python -m venv fastapienv

. ./fastapienv/bin/activate
```
5. Install packagges using `pip`
```bash
pip install -r requirements.txt
```

# Run application

To run application use standard FastAPI process
```bash
uvicorn main:app --reload
```