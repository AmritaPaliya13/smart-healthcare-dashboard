import random
import time
import requests
import json

FOG_NODE_URL = "http://localhost:5000/receive-data"  # We'll replace this in next phase

def generate_vitals():
    return {
        "patient_id": "P001",
        "heart_rate": random.randint(60, 100),        # bpm
        "temperature": round(random.uniform(97.0, 99.5), 1),  # °F
        "spo2": random.randint(94, 100),              # %
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def send_data():
    while True:
        vitals = generate_vitals()
        try:
            response = requests.post(FOG_NODE_URL, json=vitals)
            print(f"[✓] Sent: {vitals} | Status: {response.status_code}")
        except Exception as e:
            print(f"[X] Failed to send data: {e}")
        time.sleep(5)  # Wait 5 seconds before sending next data

if __name__ == "__main__":
    send_data()
