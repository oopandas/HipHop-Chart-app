from django.shortcuts import render
from django.http import JsonResponse
import requests


def get_chart_data(request):
    API_KEY = "a027a9b7e2ffaeac2d5897f8b20f9348"
    url = f"https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=hiphop&api_key={API_KEY}&format=json"

    try:
        # APIリクエスト(タイムアウト5秒)
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        tracks = data["tracks"]["track"]
    except Exception as e:
        # 失敗したらモックデータ
        tracks = [
            {"name": "Mock Song 1", "artist": {"name": "Mock Artist A"}},
            {"name": "Mock Song 2", "artist": {"name": "Mock Artist B"}},
        ]
    chart = []
    # 曲名とアーティストを10件表示
    for i, track in enumerate(tracks[:10], start=1):
        chart.append({
            "rank": i,
            "title": track["name"],
            "artist": track["artist"]["name"]
        })

    return render(request, "chart/chart_list.html", {"chart": chart})




