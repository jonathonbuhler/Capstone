from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fetch import fetch_laptop, Laptop
import pandas as pd
import numpy as np

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

@app.post("/admin/add")
async def add_laptop(laptop: Laptop):
    data = pd.read_csv("data.csv")
    if laptop.asin in data['asin'].values:
        return({"error": "Laptop already exists"})
    
    new_row = laptop.dict()
    data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
    data.to_csv("data.csv", index=False)
    return {"message": "Laptop added successfully"}

@app.get("/load/{asin}")
async def load_laptop(asin: str):
    data = pd.read_csv("data.csv")
    row = data[data["asin"] == asin]
    if row.empty:
        return {"error": "Could not locate laptop."}
    return row.iloc[0].to_dict()

@app.get("/load-all")
async def load_laptops():
    data = pd.read_csv("data.csv")
    
    return data.to_dict(orient="records")
    