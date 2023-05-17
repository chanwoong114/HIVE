from rest_framework import serializers
from .models import *

class movieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_field = ['Like_user', 'genres']