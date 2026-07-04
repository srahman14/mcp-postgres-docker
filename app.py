import os
import psycopg2
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="Dockerized Postgres API")

def get_db_connection():
    # Use 'localhost' when running python locally, or 'my-db' if running inside Docker!
    db_host = os.getenv("DB_HOST", "localhost")
    return psycopg2.connect(
        host=db_host,
        database=os.getenv("DB_NAME", "nextwork"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "secretpass123"),
        port="5432"
    )

@app.get("/")
def read_root():
    return {"message": "API is online and connected to the container network!"}

@app.get("/users")
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, role FROM users;")
        records = cursor.fetchall()
        
        users_list = []
        for row in records:
            users_list.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "role": row[3]
            })
            
        cursor.close()
        conn.close()
        return {"users": users_list}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")