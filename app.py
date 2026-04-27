import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
PLATFORM_NAME = os.getenv("PLATFORM_NAME")
PLATFORM_KEY = os.getenv("PLATFORM_KEY")
PLATFORM_SECRET = os.getenv("PLATFORM_SECRET")
CALLBACK_URL = os.getenv("CALLBACK_URL")


def initiate_handshake():
    url = f"{BASE_URL}/initiate-handshake"

    payload = {
        "platform_name": PLATFORM_NAME,
        "platform_key": PLATFORM_KEY,
        "platform_secret": PLATFORM_SECRET,
        "callback_url": CALLBACK_URL
    }

    response = requests.post(url, json=payload)
    data = response.json()

    print("\n--- Initiate Handshake Response ---")
    print(data)

    if data.get("success"):
        return data["data"]["handshake_token"]
    else:
        return None


def complete_handshake(token):
    url = f"{BASE_URL}/complete-handshake"

    payload = {
        "handshake_token": token,
        "platform_key": PLATFORM_KEY
    }

    response = requests.post(url, json=payload)
    data = response.json()

    print("\n--- Complete Handshake Response ---")
    print(data)


def main():
    print("Starting Afyanalytics Integration...\n")

    token = initiate_handshake()

    if token:
        complete_handshake(token)
    else:
        print("Handshake failed.")


if __name__ == "__main__":
    main()