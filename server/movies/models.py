from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    rating_total = models.IntegerField(default=0, null=True)
    Like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='rated_movies')
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title}:{self.genre_ids}'
    
class CommentMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=True)
    rating = models.FloatField(validators=[MinValueValidator(0, 1), MaxValueValidator(10.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)