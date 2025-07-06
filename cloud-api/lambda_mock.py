from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/receive-cloud-data")
async def receive_cloud_data(request: Request):
    data = await request.json()
    print(f"☁️ Cloud received data: {data}")
    return {"message": "Data stored successfully"}
