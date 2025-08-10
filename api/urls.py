from django.urls import path
from .views import *

urlpatterns = [
    # Trails URLS
    path('trails/', TrailListAPIView.as_view()),
    path('trails/<str:pk>/', TrailDetailAPIView.as_view()),
    
    # Steps vinculados à trilha
    path('trails/<int:trail_id>/steps/', StepListCreateForTrail.as_view(), name='trail-steps'),
    path('steps/<int:pk>/', StepDetail.as_view(), name='step-detail'),
]