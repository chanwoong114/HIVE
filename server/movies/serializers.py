from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentMovie
        fields = '__all__'
        read_only_fields = ['user', 'movie']

class movieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class movieDetailSerializer(serializers.ModelSerializer):

    class genreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    class castSerializer(serializers.ModelSerializer):
        class Meta:
            model = Cast
            fields = ['id', 'name', 'profile_path', 'character']

    class crewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Crew
            fields = '__all__'
    
    genre_ids = genreSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    crew_ids = crewSerializer(read_only=True)
    cast_ids = castSerializer(many=True, read_only=True)
    recommends = serializers.IntegerField(source='recommends.count', read_only=True)
    recommend_movies = movieListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


