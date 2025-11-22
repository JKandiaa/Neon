from dotenv import load_dotenv
import os
import psycopg
from pathlib import Path

# load .env from project root
load_dotenv(Path(r"d:/Neon/.env"))

print("Checking DB environment variables:")
print("  PGHOST=", os.getenv("PGHOST"))
print("  PGUSER=", os.getenv("PGUSER"))
print("  PGNAME=", os.getenv("PGNAME"))

try:
    conn = psycopg.connect(
        host=os.getenv("PGHOST"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        dbname=os.getenv("PGNAME", "neondb"),
        port=int(os.getenv("PGPORT", "5432")),
        connect_timeout=10,
    )
    print("Connection succeeded")
    conn.close()
except Exception as e:
    print("Connection failed:", type(e).__name__, e)
