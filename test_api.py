import requests

API_KEY = "a027a9b7e2ffaeac2d5897f8b20f9348"
URL = f"https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=hiphop&api_key={API_KEY}&format=json"

response = requests.get(URL)
data = response.json()

# 曲名とアーティストを10件表示
for i, track in enumerate(data["tracks"]["track"][:10], start=1):
    print(f"{i}位: {track["name"]} / {track["artist"]["name"]}")