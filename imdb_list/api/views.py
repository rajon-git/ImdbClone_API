from django.shortcuts import render
from imdb_list.models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request,id):
    movie = Movie.objects.get(pk=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)