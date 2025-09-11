from django.contrib import admin
from django.urls import path
from chart import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chart/", views.get_chart_data),
]
