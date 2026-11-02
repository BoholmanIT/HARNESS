from fastapi import FastAPI



app = FastAPI()


@app.get("/health")
def health_get():
    return {"status": "Ok"}