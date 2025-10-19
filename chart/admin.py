from django.contrib import admin
from .models import ChartModel

#管理画面でデータを追加、削除、編集できる
admin.site.register(ChartModel)

# Register your models here.
