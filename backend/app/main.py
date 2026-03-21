"""
Building a production-grade API
for BOOKSHELF and book keeping 

"""

# let's import the initial APIs for the endpoints 
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List



app = FastAPI(title="Personal Bookshelf API")

# --- ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "Welcome to your Personal Bookshelf API"}

@app.get("/health")
def health_check():
    return {"status": "online", "database": "connected"}

# 1. Get all books
@app.get("/v1/books")
def get_books(db: Session = Depends(database.get_db)):
    books = db.query(models.Book).all()
    return books