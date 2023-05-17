from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import *

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .serializers import *
from .models import *
import random

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = movieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def random_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = random.sample(movies, 20)
        serializer = movieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def recommend_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)

        C = Movie.objects.aggregate(Sum('vote_average'))['vote_average__sum']/(len(movies))
        m = Movie.objects.order_by('vote_count')[int(0.9*len(movies))].vote_count
        
        def weight_rating(movie):
            v = movie.vote_count
            R = movie.vote_average
            return (v/(v+m) * R) + (m/(m+v) * C)

        movies.sort(key=lambda x: weight_rating(x), reverse=True)

        serializer = movieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        serializer = movieListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)