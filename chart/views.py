from django.shortcuts import render
from django.http import JsonResponse
import requests


def get_chart_data(request):
    API_KEY = "a027a9b7e2ffaeac2d5897f8b20f9348"
    url = f"https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=hiphop&api_key={API_KEY}&format=json"
    response = requests.get(url)
    data = response.json()

    chart = []
    # 曲名とアーティストを10件表示
    for i, track in enumerate(data["tracks"]["track"][:10], start=1):
        chart.append({
            "rank": i,
            "title": track["name"],
            "artist": track["artist"]["name"]
        })

    return render(request, "chart/chart_list.html", {"chart": chart})



