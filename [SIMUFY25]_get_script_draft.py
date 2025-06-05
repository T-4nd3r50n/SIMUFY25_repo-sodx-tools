import requests
import json
from config import VX_SRC, CTX_HDR

# Internal script to retrieve structured menu data

url = "https://api-gdp.sodexonet.com/menu"

headers = {
    "Accept": "application/json",
    "X-VX-SRC": VX_SRC,
    "X-CTX-HDR": CTX_HDR
}

def fetch_menu():
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data:
                print("[INFO] Payload successfully retrieved.")
                print(json.dumps(data[:3], indent=2))  # limited output
            else:
                print("[WARNING] No data returned.")
        else:
            print(f"[ERROR] HTTP {response.status_code} during retrieval.")
    except Exception as e:
        print(f"[EXCEPTION] Could not complete request: {e}")

if __name__ == "__main__":
    fetch_menu()