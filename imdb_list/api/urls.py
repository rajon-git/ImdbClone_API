from django.urls import path
# from .views import movie_list, movie_details
from .views import WatchListAV, WatchListDetailAV, StreamPlatformAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name="movie_list"),
    path('<int:id>/', WatchListDetailAV.as_view(), name="movie_details"),
    path('stream/', StreamPlatformAV.as_view(), name="stream"),

    path('review/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
]
