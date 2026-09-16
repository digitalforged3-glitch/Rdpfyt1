import requests
import random
import string
import time
import os
from threading import Thread
from flask import Flask

# --- RENDER PORT BYPASS SERVER ---
app = Flask('')

@app.route('/')
def home():
    return "RDP Fight Server is Live!"

def run_dummy_server():
    # Render automatic 'PORT' variable deta hai, hum use use karenge
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
# ---------------------------------

# --- TOKENS (Render dashboard se uthayege) ---
SESSION_ID = os.environ.get('SESSION_ID')
CSRF_TOKEN = os.environ.get('CSRF_TOKEN')

headers = {
    'user-agent': 'Instagram 150.0.0.0.000 Android (29/10; 480dpi; 1080x2340; Xiaomi/Redmi; Redmi Note 8 Pro; begonia; qcom; en_US; 231456565)',
    'cookie': f'sessionid={SESSION_ID}; csrftoken={CSRF_TOKEN};',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'x-csrftoken': CSRF_TOKEN,
    'x-ig-app-id': '1217981644879628',
}

def generate_context():
    return ''.join(random.choices(string.digits, k=19))

def generate_random_string():
    return ''.join(random.choices(string.ascii_letters, k=4))

def start_mobile_fight():
    # Pehle 10 second ka wait karenge taaki Render ka web server stable ho jaye
    print("⚔️ DUMMY SERVER OK! WAITING FOR DEPLOYMENT ACCEPATANCE... ⚔️\n")
    time.sleep(10)
    print("🚀 BOT ACTIVE! FIRING SPAM HITS NOW... 🚀\n")
    
    while True:
        unique_id = generate_random_string()
        random_num = random.randint(100, 999)
        full_text = f"[{unique_id}] chl ht teri bhes ki tang .. {random_num}"
        
        data = {
            'text': full_text,
            'client_context': generate_context()
        }
        
        try:
            response = requests.post(
                "https://instagram.com", 
                headers=headers, 
                data=data, 
                timeout=10
            )
            if response.status_code == 200:
                print(f"[✅ CLOUD HIT SUCCESS] -> {full_text}")
            else:
                print(f"[❌ Drop/Block] -> Status: {response.status_code}")
        except Exception as e:
            print(f"[❌ Network Error] -> {e}")
            
        time.sleep(2.0)

if __name__ == "__main__":
    # 1. Dummy Web Server ko background thread me chalu karenge Render ko pass karne ke liye
    server_thread = Thread(target=run_dummy_server)
    server_thread.start()
    
    # 2. Main bot loop shuru karenge jo text fire karega
    start_mobile_fight()
    
