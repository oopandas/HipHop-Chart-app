from django import forms 
from .models import ChartModel

class ChartForm(forms.ModelForm):
    class Meta:
        model = ChartModel
        fields = ["title", "artist", "genres", "ranking", "release_date"]

    def __str__(self):
        return f"{self.title} - {self.artist}"