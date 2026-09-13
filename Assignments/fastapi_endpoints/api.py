## importing modules ##
from fastapi import FastAPI
app = FastAPI()

## home route ##

@app.get("/")
def home():
    return {
        "message": " welcome to this website! "}

## about route ##

@app.get("/about")
def about():
    return {
        "contact no.": 123-456-7890,
        "email": "example@example.com",
        "location": "east coast"
    }

## services route ##

@app.get("/services")
def services():
    return {
        "service1": "personal grooming",
        "service2": "communication skills",
        "service3": "tech skills"
    }

## skills route ##

@app.get("/docs")
def docs():
    return {
        "documentation": "This is the documentation for the skills."
    }
