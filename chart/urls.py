from django.urls import path
from . import views

app_name = "chart"

urlpatterns = [
    path("", views.get_chart_data, name="chart_list"),
]
