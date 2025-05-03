# logic_api.py
from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

class QuoteRequest(BaseModel):
    brand: str
    euro_price: int

@app.post("/calculate")
def calculate_quote(data: QuoteRequest):
    # 品牌退稅比例
    brand_tax = {
        "CHANEL": 0.94, "Louis Vuitton": 0.94, "HERMES": 0.94,
        "DIOR": 0.87, "CELINE": 0.87, "GUCCI": 0.87,
        "YSL": 0.87, "LOEWE": 0.87, "BURBERRY": 0.87,
        "CHLOÉ": 0.87, "MIU MIU": 0.85, "BALENCIAGA": 0.87, "其他": 1.0
    }

    rate = 36  # 匯率固定，可於後端更新
    tax = brand_tax.get(data.brand, 1.0)
    euro = data.euro_price
    after_tax = euro * tax

    # 運費與利潤邏輯
    if euro < 600:
        shipping, profit = 15, 1000
    elif euro < 800:
        shipping, profit = 15, 2000
    elif euro < 1000:
        shipping, profit = 20, 2500
    elif euro <= 1500:
        shipping, profit = 20, 3000
    else:
        shipping, profit = 25, 3500

    total = after_tax + shipping
    tw_price = math.ceil((total * rate + profit) / 100) * 100

    return {"final_price": tw_price}
