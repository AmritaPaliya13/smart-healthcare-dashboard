from fastapi import FastAPI, Request
import requests

app = FastAPI()

CLOUD_API_URL = "http://localhost:8000/cloud-endpoint"  # dummy for now

@app.post("/receive-data")
async def receive_data(request: Request):
    data = await request.json()
    print(f"Received data from IoT device: {data}")

    heart_rate = data.get("heart_rate", 0)
    spo2 = data.get("spo2", 0)

    if heart_rate < 60 or heart_rate > 100 or spo2 < 95:
        print("⚠️  Critical vitals detected at Fog layer! (notifying locally)")
    else:
        try:
            res = requests.post(CLOUD_API_URL, json=data)
            print(f"✅ Data forwarded to Cloud: {res.status_code}")
        except Exception as e:
            print(f"❌ Failed to send to cloud: {e}")

    return {"status": "received"}

