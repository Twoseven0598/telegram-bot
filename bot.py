import requests
import time
import telegram

# Konfigurasi
TOKEN = "7942894356:AAGrKds6UB2GJR8o-Y-QqFLfmeUObmaPeyI"
CHAT_ID = "5094000766"
API_URL = "https://www.mexc.com/open/api/v2/market/deals?symbol=XEP_USDT"

bot = telegram.Bot(token=TOKEN)

def get_latest_trade():
    response = requests.get(API_URL)
    data = response.json()
    if "data" in data and data["data"]:
        return data["data"][0]  # Ambil transaksi terbaru
    return None

last_trade_id = None

while True:
    trade = get_latest_trade()
    if trade and trade["id"] != last_trade_id:
        last_trade_id = trade["id"]
        message = f"📈 XEP Buy Alert!\nHarga: {trade['price']} USDT\nJumlah: {trade['quantity']} XEP"
        bot.send_message(chat_id=CHAT_ID, text=message)

    time.sleep(10)  # Cek setiap 10 detik
