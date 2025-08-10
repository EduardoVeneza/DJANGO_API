from django.urls import path
from .views import TrailListAPIView, TrailDetailAPIView, TrailCreateAPIView

urlpatterns = [
    path('trails/', TrailListAPIView.as_view(), name='trail-list'),
    path('trails/<str:pk>/', TrailDetailAPIView.as_view(), name='trail-detail'),
    path('trails/add/', TrailCreateAPIView.as_view(), name='trail-add'),
]
