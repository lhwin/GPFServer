import requests
import json

base_url = "http://127.0.0.1:8000"

item_data = {
    "satelite_dir":"/home/leehir/data/satelite",
    "oceantide_dir":"/home/leehir/data/oceantide"
}

response = requests.post(f"{base_url}/data/discover", json=item_data)
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))
