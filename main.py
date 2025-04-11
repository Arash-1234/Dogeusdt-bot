import os
import time
import requests

def get_price():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT")
    return float(response.json()["price"])

while True:
    price = get_price()
    print("Current DOGE Price:", price)
    time.sleep(300)  # هر 5 دقیقه
