from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=500)
    title_en = models.CharField(max_length=500)
    audience = models.IntegerField()
    open_date = models.DateTimeField()
    genre = models.CharField(max_length=250)
    watch_grade = models.FloatField()
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()