from django.shortcuts import render
from imdb_list.models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data = request.data)  #data received from user, user send data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def movie_details(request,id):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return Response({'message': f'{movie.name} removed successfully'})