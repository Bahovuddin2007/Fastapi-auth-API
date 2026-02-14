from fastapi import FastAPI

app = FastAPI(title="FastAPI Auth API")

@app.get("/health")
def health():
    return {"status": "ok"}
