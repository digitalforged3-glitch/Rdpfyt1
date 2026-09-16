import requests
import random
import string
import time
import os

# --- TOKEN SECURITY BYPASS ---
# Render ke dashboard se automatic aur safely uthaye jayenge
SESSION_ID = os.environ.get('SESSION_ID')
CSRF_TOKEN = os.environ.get('CSRF_TOKEN')
# -------------------------------

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
    print("⚔️ NEW FRESH CLOUD SERVER STARTED SUCCESSFULLY! ⚔️\n")
    
    while True:
        unique_id = generate_random_string()
        random_num = random.randint(100, 999)
        full_text = f"[{unique_id}] chl ht teri bhes ki tang .. {random_num}"
        
        data = {
            'text': full_text,
            'client_context': generate_context()
        }
        
        try:
            # Strict direct URL, isme koi string mix-up ya slash miss nahi ho sakta
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
            
        time.sleep(2.0) # Server stability ke liye 2 seconds ka gap rakha hai

if __name__ == "__main__":
    start_mobile_fight()
  
