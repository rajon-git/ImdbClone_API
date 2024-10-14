from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import movie_list, movie_details
from .views import (WatchListAV, WatchListDetailAV, StreamPlatformAV, 
                    ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS,basename='streamPlatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name="movie_list"),
    path('<int:id>/', WatchListDetailAV.as_view(), name="movie_details"),
    # path('stream/', StreamPlatformAV.as_view(), name="stream"),

    path('', include(router.urls)),

    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),

    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name="review-list"),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
]
