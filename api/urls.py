from django.urls import path
from .views import *

urlpatterns = [
     # Links por step
    path('steps/<int:step_id>/links/', LinkListCreateAPIView.as_view(), name='link-list-create'),
    path('links/<int:pk>/', LinkDetailAPIView.as_view(), name='link-detail'),

    # Attachments por step
    path('steps/<int:step_id>/attachments/', AttachmentListCreateAPIView.as_view(), name='attachment-list-create'),
    path('attachments/<int:pk>/', AttachmentDetailAPIView.as_view(), name='attachment-detail'),

    # Trails URLS
    path('trails/', TrailListAPIView.as_view()), # 100% TESTADOS, TRATADOS E FUNCIONAIS
    path('trails/<str:pk>/', TrailDetailAPIView.as_view()), # 100% TESTADOS, TRADADOS E FUNCIONAIS
    
    # Steps vinculados à trilha
    path('trails/<int:trail_id>/steps/', StepListCreateForTrail.as_view(), name='trail-steps'), # 100% TESTADOS, TRATADOS E FUNCIONAIS
    path('steps/<int:pk>/', StepDetail.as_view(), name='step-detail'), # 100% TESDADOS, TRATADOS E FUNCIONAIS
]