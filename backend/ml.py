import asyncio
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

df = None
rf = None
sc = None

async def train(laptops):
    global df, rf, sc
    df = pd.DataFrame(laptops)
    df = df.set_index("id")
    df = pd.get_dummies(df, columns=["ram_type"])
    df["pixel_count"] = df["screen_width"] * df["screen_height"]    
    X = df.drop(columns=["price", "screen_width", "screen_height"])
    y = df["price"]
    sc = StandardScaler()
    sc.fit(X)
    X = sc.transform(X)
    rf = RandomForestRegressor(random_state=42, n_estimators=100)
    rf.fit(X,y)
    df.to_csv("ml.csv")
    fair_price = rf.predict(X)
    for i,p in enumerate(fair_price):
        fair_price[i] = round(p, 2)
    df["fair_price"] = fair_price
    return df

async def predict_fair(laptop):
    global df, rf, sc    
    ldf = pd.DataFrame([laptop.dict()])        
    ldf["pixel_count"] = ldf["screen_width"] * ldf["screen_height"]
    ldf = ldf.drop(columns=["fair_price", "screen_width", "screen_height", "id", "brand", "asin", "cpu", "gpu", "img_url", "model_name", "model_number", "price", "title"])
    ldf = pd.get_dummies(ldf, columns=["ram_type"])
    ldf = ldf.reindex(columns=df.columns, fill_value=0)
    ldf = ldf.drop(columns=["fair_price", "price", "screen_height", "screen_width"])
    X = sc.transform(ldf) 
    return float(rf.predict(X)[0])
    





