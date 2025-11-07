from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "🚀 Image updated via CI/CD"} + str(datetime.datetime.now())}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/info")
async def info():
    return {
        "app_name": "Hello App CI/CD",
        "author": "Gustavo Hossein",
        "environment": "production"
    }
