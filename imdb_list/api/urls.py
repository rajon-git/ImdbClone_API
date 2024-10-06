from django.urls import path
# from .views import movie_list, movie_details
from .views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name="movie_list"),
    path('<int:id>/', MovieDetailAV.as_view(), name="movie_details"),
]
