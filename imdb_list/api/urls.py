from django.urls import path
# from .views import movie_list, movie_details
from .views import WatchListAV, WatchListDetailAV, StreamPlatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name="movie_list"),
    path('<int:id>/', WatchListDetailAV.as_view(), name="movie_details"),
    path('stream/', StreamPlatformAV.as_view(), name="stream"),
]
