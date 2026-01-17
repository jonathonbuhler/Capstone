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
    storage_capacity: Optional[int] = 0
    cpu: Optional[str] = ""
    cpu_cores: Optional[int] = 0
    cpu_clock: Optional[float] = 0.0
    ram_type: Optional[str] = ""
    ram_capacity: Optional[int] = 0
    touch_screen: Optional[bool] = False
    screen_size: Optional[float] = 0.0
    screen_width: Optional[int] = 0
    screen_height: Optional[int] = 0
    screen_refresh: Optional[int] = 0
    battery_capacity: Optional[int] = 0
    year: Optional[int] = 0
    gpu_type: Optional[bool] = None
    gpu: Optional[str] = ""
    rating: Optional[float] = 0.0
    price: Optional[float] = 0.0

def fetch_laptop(asin):
    url = f"https://amazon.com/dp/{asin}"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    if resp.status_code != 200:
        return Laptop(asin=asin)

    soup = BeautifulSoup(resp.text, "html.parser")

    
    title_tag = soup.select_one("#productTitle")
    price_tag = soup.select_one(".a-price .a-offscreen")
    rating_tag = soup.select_one("#averageCustomerReviews .a-icon-alt") \
             or soup.select_one(".averageStarRating .a-icon-alt")
    
    tech_details = {}

    # 1. Tech Spec Section
    for section_id in ["productDetails_techSpec_section_1", "productDetails_techSpec_section_2"]:
        rows = soup.select(f"#{section_id} tr")
        for row in rows:
            key = row.select_one("th")
            val = row.select_one("td")
            if isinstance(val,str):
                val = val.replace("\u200e", "")
            if key and val:
                tech_details[key.get_text(strip=True).lower()] = val.get_text(strip=True)

    # 2. Detail Bullets Section
    detail_rows = soup.select("#productDetails_detailBullets_sections1 tr")
    for row in detail_rows:
        key = row.select_one("th")
        val = row.select_one("td")
        if isinstance(val,str):
            val = val.replace("\u200e", "")
        if key and val:
            tech_details[key.get_text(strip=True).lower()] = val.get_text(strip=True)

    # 3. Feature bullets fallback (some specs are here)
    bullets = soup.select("#feature-bullets ul li span")
    for b in bullets:
        text = b.get_text(strip=True)
        if ":" in text:  # naive key: value
            k, v = map(str.strip, text.split(":", 1))
            if isinstance(v,str):
                v = v.replace("\u200e", "")
            tech_details[k.lower()] = v

    print(tech_details)  # debug

    
    storage_capacity = tech_details.get("hard drive")
    storage_capacity = storage_capacity.replace("SSD","")
    storage_capacity = storage_capacity.replace("\u200e", "")
    if "TB" in storage_capacity:
        storage_capacity = int(storage_capacity.replace("TB", "").strip())*1000
    elif "GB" in storage_capacity:
        storage_capacity = int(storage_capacity.replace("GB", "").strip())
    
    
    cpu_cores = tech_details.get("number of processors")
    cpu_cores = cpu_cores.replace("\u200e", "")

    rating = rating_tag.get_text(strip=True) if rating_tag else None
    rating = rating[0:2]
    
    screen_size = tech_details.get("standing screen display size")
    screen_size = screen_size.replace("\u200e", "")
    screen_size = screen_size.replace("Inches", "")

    price = price_tag.get_text(strip=True) if price_tag else None
    price = price.replace("$", "")
    price = price.replace(",", "")

    ram_capacity = tech_details.get("ram")
    ram_capacity = ram_capacity.replace("GB","").replace("\u200e","").replace("DDR5","").replace("DDR4","").replace("LP","")

    screen_width = tech_details.get("screen resolution")
    screen_width = screen_width.replace("\u200e","").replace("pixels","")
    screen_width = screen_width.split("x")[0]
    
    screen_height = tech_details.get("screen resolution")
    screen_height = screen_height.replace("\u200e","").replace("pixels","")
    screen_height = screen_height.split("x")[1]

    gpu_type = tech_details.get("card description")
    gpu_type = gpu_type.replace("\u200e","").strip()    
    gpu_type = gpu_type == "Dedicated"
    

    return Laptop(        
        asin=asin,
        title=title_tag.get_text(strip=True) if title_tag else "",
        model_name=tech_details.get("model name"),
        model_number=tech_details.get("series"),
        price=price,        
        storage_capacity=storage_capacity,
        cpu=tech_details.get("processor series"),
        cpu_cores=cpu_cores,
        ram_type=tech_details.get("computer memory type"),
        ram_capacity=ram_capacity,
        brand=tech_details.get("brand"),
        year=tech_details.get("model year"),
        touch_screen=tech_details.get("touch screen type"),
        screen_size=screen_size,
        screen_width=screen_width,
        screen_height=screen_height,
        screen_refresh=tech_details.get("refresh rate"),
        battery_capacity=tech_details.get("lithium-battery energy content"),
        gpu_type=gpu_type,
        gpu=tech_details.get("graphics coprocessor"),
        rating=rating
    )
