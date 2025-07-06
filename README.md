README.md

🧠 Smart Healthcare Dashboard

A full-stack real-time healthcare monitoring system using **IoT**, **Fog Computing**, and **Cloud APIs**, with a live dashboard built using **FastAPI** and **Jinja2**.

📌 Project Overview

This system simulates real-time patient vitals using a Python IoT simulator. Data is sent to a fog computing layer for preprocessing and anomaly detection. From there, it's forwarded to a cloud API which stores and visualizes the data on a live web dashboard.

🔧 Features

- 📟 **IoT Device Simulator**: Generates random patient vitals (heart rate, SpO2)
- 🌫️ **Fog Node (Edge Layer)**: FastAPI service that processes vitals and detects anomalies
- ☁️ **Cloud API**: Simulated cloud endpoint (FastAPI) to receive, store and display data
- 📊 **Web Dashboard**: Live HTML/Jinja2 dashboard showing recent vitals
- 🚨 **Critical Alerts**: Automatically highlights abnormal values
- 🧪 Easy to test, extend and deploy on AWS Lambda or similar platforms

📂 Folder Structure
smart-healthcare-dashboard
├── iot-device-simulator
│ └── device_simulator.py
├── fog-node
│ └── app.py
├── cloud-api
│ ├── app.py
│ └── templates
│ └── dashboard.html
├── screenshots
├── README.md

🚀 How to Run

-Terminal 1 – Start Fog Node
cd fog-node
uvicorn app:app --host 0.0.0.0 --port 5000

-Terminal 2 – Start IoT Device Simulator
cd iot-device-simulator
python device_simulator.py

-Terminal 3 – Start Cloud API + Dashboard
cd cloud-api
uvicorn app:app --host 0.0.0.0 --port 8000

~Then visit http://localhost:8000 to view the live dashboard!

📦 Requirements
Install dependencies:

pip install fastapi uvicorn jinja2


