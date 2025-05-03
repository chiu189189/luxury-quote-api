import streamlit as st
import requests

st.set_page_config(page_title="📦 批發報價系統", layout="centered")
st.title("📦 批發報價系統")

# 品牌選單
brands = ["CHANEL", "Louis Vuitton", "HERMES", "DIOR", "CELINE", "GUCCI", "YSL", "LOEWE", "BURBERRY", "CHLOÉ", "BALENCIAGA", "其他"]

brand = st.selectbox("選擇品牌", brands)
euro_price = st.number_input("輸入商品歐元原價", min_value=0, step=1)

if st.button("計算報價"):
    res = requests.post(
        "https://luxury-quote-api.onrender.com/calculate",
        json={"brand": brand, "euro_price": euro_price}
    )

    if res.status_code == 200:
        tw_price = res.json().get("final_price")
        st.success(f"{brand} 報價：NT$ {tw_price:,}")
    else:
        st.error("報價失敗，請稍後再試。")
