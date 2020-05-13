from django.db import models
from movies.models import Movie
from django.conf import settings

# Create your models here.
class Review(models.Model):
    CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='reviews')
    content = models.TextField()
    rank = models.IntegerField(choices=CHOICES)
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='comments')
