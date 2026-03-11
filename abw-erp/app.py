from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ABW Construction ERP is running"}
