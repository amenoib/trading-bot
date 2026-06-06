import requests

BOT_TOKEN = "8950109676:AAEFjGnE09PSErDBLFAhr92G6Z_3w6lb3b4"
CHAT_ID = "8809238477"

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
