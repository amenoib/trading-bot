import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    response = requests.post(url, data=data)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code != 200:
        raise Exception(f"Telegram gönderim hatası: {response.text}")

def main():
    send_telegram("✅ Bot çalışıyor! İlk test mesajı")

if __name__ == "__main__":
    main()
