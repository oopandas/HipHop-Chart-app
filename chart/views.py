from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import ChartModel


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

def home_view(request):
    return render(request, "chart/home.html")

def genres_view(request):
    genres = ["HipHop", "R&B", "Rock", "Reggae", "Pop"]
    # genresのリストをgenres.htmlに渡す
    return render(request, "chart/genres.html", {"genres": genres})

def history_view(request):
    history = [
        {"title": "Mock Song 1", "artist": {"name": "Mock Artist A"}, "data": "2025-10-06"},
        {"title": "Mock Song 2", "artist": {"name": "Mock Artist B"}, "data": "2025-10-06"},
    ]
    # historyのリストをhistory.htmlに移す
    return render(request, "chart/history.html", {"history":history})

def about_view(request):
    # 固定情報は最初から辞書型
    context = {
        "app_name": "HipHop Chart Viewer",
        "author": "kumagai",
        "description": "このアプリはLast.fm APIから取得したHipHopチャートを自動で取得・表示します"
    }
    # 辞書で渡しているので引数は変数名でOK
    return render(request, "chart/about.html", context)

def chart_information_view(request):
    # ChartModelのデータを全て取得
    chart_information = ChartModel.objects.all()
    # テンプレートに渡す
    return render(request, "chart/chart_information.html", {"chart_information":chart_information})    





