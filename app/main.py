from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="E-commerce API", description="Learning project for backend development", version="1.0.0")


#ZASTO: CORS - dozvoljava frontendu da pozova nas api 
# Bez ovoga browser blokira requests
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],)

#ZASTO: Health check endpoint - da proveris da li API radi
@app.get("/")
def read_root():
    """
    ZASTO: Svaki API treba health check
    - Deploy servisi koriste ovo
    - Ti koristis da proveris da li radi
    """
    return {"status": "running", "message": "E-commerece api"}

#ZASTO: Verzionisanje API-ja best practice
@app.get("api/v1/health")
def health_check():
    return {"status": "healthy"}
