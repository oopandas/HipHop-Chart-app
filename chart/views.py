from django.shortcuts import render
from django.http import JsonResponse

def get_chart_data(request):
    #モックデータ(仮のチャート情報)
    mock_data = [
            {"rank": 1, "title": "Mock Song 1", "artist": "Mock Artist A"},
            {"rank": 2, "title": "Mock Song 2", "artist": "Mock Artist B"},
            {"rank": 3, "title": "Mock Song 3", "artist": "Mock Artist C"},
    ]
    # TODO: APIからデータ取得して返す
    return render(request, "chart/chart_list.html", {"chart": mock_data})
# Create your views here.
