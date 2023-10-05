import requests

res = requests.post(
    "https://agent1-api.onrender.com",
    json={
        "query": "Metas latest products and news"
    }
).json()

print(res)