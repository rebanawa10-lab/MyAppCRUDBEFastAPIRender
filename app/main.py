# file:    main.py 

#Local PC MS SQL Server. Ok
#from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


#Supabase config
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
#from sqlalchemy import text


#Local PC MS SQL Server. Ok
#from .database import engine

#Supabase config
from .database import engine, get_db

from . import models
# OLD:
#from app.api.routes.user import router as user_router

# NEW:
# Import routers
from .api.routes import user, inventory

# Create database tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OLD
# INCLUDE ROUTER
#app.include_router(user_router, prefix="/users", tags=["Users"])

# NEW:
# Include routers
app.include_router(user.router)
app.include_router(inventory.router)


@app.get("/")
def root():
    return {"message": "FastAPI is running"}

#Supabase config
@app.get("/testdb")
def test_db(db: Session = Depends(get_db)):
    result = db.execute("SELECT 1").scalar()
    return {"status": "connected" if result == 1 else "failed"}