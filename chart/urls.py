from django.urls import path
from . import views

app_name = "chart"

urlpatterns = [
    # path("", views.get_chart_data, name="chart_list"),
    path("", views.home_view, name="home"),
    path("genres/", views.genres_view, name="genres"),
    path("history/", views.history_view, name="history"),
    path("about/", views.about_view, name="about"),
    path("chart_information/", views.chart_information_view, name="chart_information"),
]
