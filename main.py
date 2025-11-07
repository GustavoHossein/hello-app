from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "✅ CI/CD Pipeline Working!",
        "version": "2.0.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "environment": "production"}

@app.get("/info")
async def info():
    return {
        "app": "FastAPI CI/CD Demo",
        "author": "Gustavo Hossein",
        "deployment": "automated"
    }
