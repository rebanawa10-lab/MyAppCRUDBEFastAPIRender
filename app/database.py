# file:         database.py

#Supabase config
from dotenv import load_dotenv
import os



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Supabase config
# Load .env file
load_dotenv()

#Local PC MS SQL Server. Ok
# DATABASE_URL = (
#     "mssql+pyodbc://sa:86427211abc@localhost:1433/AzureSQL"
#     "?driver=ODBC+Driver+17+for+SQL+Server"
# )
#engine = create_engine(DATABASE_URL)


#Supabase config
#DATABASE_URL = "postgresql://postgres:password@db.xxxxx.supabase.co:5432/postgres"
#               postgresql://postgres:5088J#@db.imvnyjrfwjeeifqvovin.supabase.co:5432/postgres
#DATABASE_URL = "postgresql://postgres:5088J#@db.imvnyjrfwjeeifqvovin.supabase.co:5432/postgres"
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")


engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# FORMAT:
# DATABASE_URL = (
#     "mssql+pyodbc://username:password@localhost:1433/YourDB"
#     "?driver=ODBC+Driver+17+for+SQL+Server"
# )
