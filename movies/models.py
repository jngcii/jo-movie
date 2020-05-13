from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.URLField(null=True, blank=True)
    description = models.TextField()

    @property
    def rank(self):
        return self.reviews.all().aggregate(models.Avg('rank')) if self.reviews.count() else 0

    def __str__(self):
        return self.title