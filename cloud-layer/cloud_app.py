from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/receive-cloud-data")
async def receive_cloud_data(request: Request):
    data = await request.json()
    print(f"✅ Received at Cloud Layer: {data}")
    # Simulate storing data
    return {"message": "Data received by cloud"}
