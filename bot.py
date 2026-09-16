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
    return "RDP Proxy Fight Server is Live!"

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
# ---------------------------------

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

# Free Proxy List (Instagram Datacenter Bypass Ke Liye)
FREE_PROXIES = [
    "http://45.77.56.124:8080",
    "http://95.179.212.190:80",
    "http://149.28.134.147:3128",
    "http://207.148.77.202:8080"
]

def generate_context():
    return ''.join(random.choices(string.digits, k=19))

def generate_random_string():
    return ''.join(random.choices(string.ascii_letters, k=4))

def start_mobile_fight():
    print("⚔️ PROXY BYPASS ENGINE ACTIVE... WAITING FOR DEPLOYMENT... ⚔️\n")
    time.sleep(10)
    
    while True:
        unique_id = generate_random_string()
        random_num = random.randint(100, 999)
        full_text = f"[{unique_id}] chl ht teri bhes ki tang .. {random_num}"
        
        data = {
            'text': full_text,
            'client_context': generate_context()
        }
        
        # Har hit par alag IP use hogi taaki ghost block na ho
        proxy = random.choice(FREE_PROXIES)
        proxy_dict = {"http": proxy, "https": proxy}
        
        try:
            response = requests.post(
                "https://instagram.com", 
                headers=headers, 
                data=data, 
                proxies=proxy_dict,
                timeout=8
            )
            
            if response.status_code == 200 and '"status":"ok"' in response.text.lower():
                print(f"[🔥 PROXY BYPASS REAL HIT] -> {full_text} via {proxy}")
            else:
                print(f"[❌ Drop Attempted By IG] -> Proxy Rotated.")
        except Exception as e:
            # Agar koi proxy slow ho ya na chale, toh loop rkega nahi, next proxy par switch ho jayega
            print(f"[🔄 Switching Proxy] -> Retrying with next IP...")
            
        time.sleep(2.5)

if __name__ == "__main__":
    server_thread = Thread(target=run_dummy_server)
    server_thread.start()
    start_mobile_fight()
    
