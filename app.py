# smart_traffic_agent.py
import cv2
from ultralytics import YOLO
import time
import requests
import json
from ibm_watson_machine_learning import APIClient
import ibm_boto3
from ibm_botocore.client import Config
import getpass

# === IBM WML CONFIGURATION ===
wml_url = input("Enter your IBM WML URL: ")
wml_apikey = getpass.getpass("Enter your IBM API Key: ")
wml_space_id = input("Enter your IBM WML Space ID: ")
model_deployment_endpoint = input("Enter your WML Model Deployment Endpoint: ")

wml_credentials = {
    "url": wml_url,
    "apikey": wml_apikey
}
wml_client = APIClient(wml_credentials)
wml_client.set.default_space(wml_space_id)

# === IBM COS CONFIGURATION ===
cos_apikey = getpass.getpass("Enter your IBM COS API Key: ")
cos_instance_id = input("Enter your IBM COS Resource Instance ID: ")
cos_endpoint = input("Enter your COS Endpoint URL: ")
bucket_name = input("Enter your COS Bucket Name: ")

cos_credentials = {
    "apikey": cos_apikey,
    "resource_instance_id": cos_instance_id,
    "endpoint": cos_endpoint,
    "iam_endpoint": "https://iam.cloud.ibm.com/identity/token"
}

cos = ibm_boto3.client("s3",
    ibm_api_key_id=cos_credentials["apikey"],
    ibm_service_instance_id=cos_credentials["resource_instance_id"],
    ibm_auth_endpoint=cos_credentials["iam_endpoint"],
    config=Config(signature_version="oauth"),
    endpoint_url=cos_credentials["endpoint"]
)

# === CONFIGURATION ===
camera_stream_url = input("Enter your camera stream URL (or leave blank for test video): ")
signal_control_api = input("Enter your traffic control API endpoint (if available): ")

# === FUNCTION DEFINITIONS ===
def detect_vehicles_ibm(frame):
    _, img_encoded = cv2.imencode('.jpg', frame)
    payload = {
        "input_data": [{"values": [img_encoded.tobytes().hex()]}]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(model_deployment_endpoint, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result.get("predictions", [{}])[0].get("vehicle_count", 0)
    else:
        print("IBM WML detection failed.")
        return 0

def upload_frame_to_cos(frame, filename):
    _, buffer = cv2.imencode(".jpg", frame)
    cos.put_object(Bucket=bucket_name, Key=filename, Body=buffer.tobytes())

def decide_traffic_signal(vehicle_count):
    if vehicle_count > 8:
        return "GREEN", 20
    elif vehicle_count > 4:
        return "YELLOW", 10
    else:
        return "RED", 5

def apply_traffic_light(color):
    if signal_control_api:
        try:
            requests.post(signal_control_api, json={"signal": color})
        except:
            print("Could not send signal change to the controller.")
    else:
        print(f"Signal change simulated: {color}")

# === AGENT EXECUTION ===
print("Smart Traffic Agent started. Press Ctrl+C to stop.")
cap = cv2.VideoCapture(camera_stream_url if camera_stream_url else 0)

if not cap.isOpened():
    print("Cannot access the camera stream. Access is required from authorities.")
else:
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to fetch frame. Check camera access.")
                continue

            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"frame_{timestamp}.jpg"
            upload_frame_to_cos(frame, filename)

            vehicle_count = detect_vehicles_ibm(frame)
            signal_color, duration = decide_traffic_signal(vehicle_count)

            print(f"Vehicles: {vehicle_count} -> Signal: {signal_color} ({duration}s)")
            apply_traffic_light(signal_color)

            time.sleep(duration)

    except KeyboardInterrupt:
        print("Agent stopped.")
    finally:
        cap.release()
