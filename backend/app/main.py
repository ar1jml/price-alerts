from fastapi import FastAPI

app = FastAPI(title="Price Alerts API")


@app.get("/")
def root():
    return {"message": "Price Alerts API is running"}