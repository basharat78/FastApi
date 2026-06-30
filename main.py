from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
        return{
            "message" : "Welcome to the StudentHub Api "
        }
    
@app.get("/about")
def about():
    return{
    "project": "StudentHub",
    "framework": "FastAPI",
    "language": "Python"
    }
@app.get("/version")
def version():
    return{
        "version": "1.0.0"
    }
