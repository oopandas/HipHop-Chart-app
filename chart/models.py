from django.db import models

# Create your models here.

class ChartModel(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=100)
    genres = models.CharField(max_length=50)
    ranking = models.IntegerField()
    release_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.title} - {self.artist}"

