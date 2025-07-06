from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Store recent vitals here
latest_data = []

@app.post("/cloud-endpoint")
async def cloud_handler(request: Request):
    data = await request.json()
    data["timestamp"] = datetime.datetime.now().strftime("%H:%M:%S")
    latest_data.append(data)
    if len(latest_data) > 10:
        latest_data.pop(0)
    print(f"🌐 Cloud received data: {data}")
    return {"status": "✅ Cloud processed the data successfully"}

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "vitals": latest_data[::-1]  # Most recent on top
    })

