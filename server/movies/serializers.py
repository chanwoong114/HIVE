from rest_framework import serializers
from .models import *

class movieListSerializer(serializers.ModelSerializer):

    class genreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    genre_ids = genreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'rating_total', 'release_date', 'vote_count', 'vote_average', 'overview', 'poster_path', 'genre_ids']