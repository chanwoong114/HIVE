from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentMovie
        fields = '__all__'
        read_only_fields = ['user', 'movie']

class movieListSerializer(serializers.ModelSerializer):

    class genreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    genre_ids = genreSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


