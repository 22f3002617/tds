from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"email": "22f3002671@ds.study.iitm.ac.in", "message": "Hello from Codespaces!"}