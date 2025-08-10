from django.urls import path
from .views import TrailListAPIView, TrailDetailAPIView

urlpatterns = [
    path('trails/', TrailListAPIView.as_view()),
    path('trails/<str:pk>/', TrailDetailAPIView.as_view()),
    # path('trails/create/', TrailCreateAPIView.as_view()),
]