import requests
from bs4 import BeautifulSoup
from typing import Optional
from pydantic import BaseModel

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


class Laptop(BaseModel):
    asin: str
    title: Optional[str] = ""
    model_number: Optional[str] = ""
    model_name: Optional[str] = ""
    brand: Optional[str] = ""
    storage_type: Optional[str] = ""
    storage_capacity: Optional[str] = ""
    cpu: Optional[str] = ""
    ram_type: Optional[str] = ""
    ram_capacity: Optional[str] = ""
    screen_size: Optional[str] = ""
    screen_width: Optional[str] = ""
    screen_height: Optional[str] = ""
    screen_refresh: Optional[str] = ""
    battery_capacity: Optional[str] = ""
    year: Optional[str] = ""
    price: Optional[str] = ""

def fetch_laptop(asin):
    url = f"https://amazon.com/dp/{asin}"
    resp = requests.get(url, headers=HEADERS, timeout=15)

    if resp.status_code != 200:
        return Laptop(asin=asin)

    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.select_one("#productTitle")
    price_tag = soup.select_one(".a-price .a-offscreen")

    bullets = soup.select("#feature-bullets ul li span")
    features = [b.get_text(strip=True) for b in bullets if b.get_text(strip=True)]    

    
    tech_details = {}
    rows = soup.select("#productDetails_techSpec_section_1 tr")
    for row in rows:
        key = row.select_one("th")
        val = row.select_one("td")
        if key and val:
            tech_details[key.get_text(strip=True).lower()] = val.get_text(strip=True)

    print(tech_details)
    
    laptop = Laptop(
        asin=asin,
        title=title_tag.get_text() if title_tag else None,
        model_name = tech_details.get("model name"),
        model_number = tech_details.get("model number"),
        price = price_tag.get_text() if price_tag else None,
        storage_type = tech_details.get("hard drive"),
        storage_capacity= tech_details.get("hard drive"),
        cpu= tech_details.get("processor series"),
        ram_type = tech_details.get("ram"),
        ram_capacity = tech_details.get("ram"),
        brand = tech_details.get("brand"),
        year= tech_details.get("model year"),
        screen_size= tech_details.get("standing screen display size"),
        screen_width= tech_details.get("screen resolution"),
        screen_height= tech_details.get("screen resolution"),
        screen_refresh= tech_details.get("refresh rate"),
        battery_capacity= tech_details.get("lithium-battery energy content")
    )

    return laptop
