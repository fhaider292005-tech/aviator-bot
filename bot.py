import requests

TOKEN = "8540467159:AAEjZfiJFr_rdoChAeMUuqdbd1aNztJScfk"
CHAT_ID = "8269072050"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🚀 Aviator Predictor Bot is running from GitHub!"
}

response = requests.post(url, data=data)

print(response.text)
