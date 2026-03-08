import requests
import os

TOKEN  = os.getenv("BOT_TOKEN")
CHAT_ID = "5843348565"

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)