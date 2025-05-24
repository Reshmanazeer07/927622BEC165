import requests

url = 'http://127.0.0.1:5000/average'
data = {
    "numbers": [10, 20, 30, 40, 50]
}

response = requests.post(url, json=data)
print("Response:", response.json())
