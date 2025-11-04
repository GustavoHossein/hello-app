from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from Mac M2!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}