import requests

# BURAYA KENDİ BİLGİLERİNİ GİR
BOT_TOKEN = "8950109676:AAEFjGnE09PSErDBLFAhr92G6Z_3w6lb3b4"
CHAT_ID = "8809238477"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

def main():
    send_telegram("✅ Bot çalışıyor! İlk test mesajı")

if __name__ == "__main__":
    main()
