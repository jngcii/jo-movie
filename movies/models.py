from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.URLField(null=True, blank=True)
    description = models.TextField()