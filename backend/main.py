from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fetch import fetch_laptop

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, PUT, etc.
    allow_headers=["*"],  # allow all headers
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/admin/{asin}")
async def load_laptop_from_amazon(asin: str):
    if len(asin) != 10:
        raise HTTPException(status_code=400, detail="Invalid Asin")
    laptop = fetch_laptop(asin)
    return laptop