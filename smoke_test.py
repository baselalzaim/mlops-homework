import requests
import sys

response = requests.get("http://localhost:8000/predict?text=hello")

if response.status_code == 200:
    print("Smoke test passed")
    sys.exit(0)
else:
    print("Smoke test failed")
    sys.exit(1)
