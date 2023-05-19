from rest_framework import serializers
from movies.models import *
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ['id', 'username']

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'title', 'poster_path']

    rated_movies = MovieSerializer(many=True, read_only=True)
    followings = FollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'rated_movies', 'profile', 'followers', 'followings', 'follower_count', 'followings_count']