from rest_framework import serializers
from movies.models import *
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'title', 'poster_path']

    rated_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'rated_movies', 'profile']