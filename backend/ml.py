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
    X = df.drop(columns=["price"])
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
    return rf.predict(laptop)
    





