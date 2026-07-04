import os
import psycopg2
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

def fetch_users():
    try:
        # Establish connection to the local Docker container
        connection = psycopg2.connect(
            host="localhost",
            database=os.getenv("DB_NAME", "nextwork"),
            user=os.getenv("DB_USER", "admin"),
            password=os.getenv("DB_PASSWORD", "secretpass123"),
            port="5432"
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, email, role FROM users;")
        records = cursor.fetchall()
        
        print("\n=== SUCCESS: Connected to Containerized PostgreSQL ===")
        print(f"Retrieved {len(records)} users:")
        print("-" * 50)
        for row in records:
            print(f"[{row[3]}] ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")
        print("-" * 50)
        
        cursor.close()
        connection.close()
        
    except Exception as error:
        print(f"Error connecting to database: {error}")

if __name__ == "__main__":
    fetch_users()
