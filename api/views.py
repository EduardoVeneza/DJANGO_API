from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TrailSerializer
from trilhas.models import Trail, Link, Step

# Create your views here.
@api_view(['GET'])
def TrailList(request):
    trails = Trail.objects.all() # Query
    serializer = TrailSerializer(trails, many=True)
    return Response(serializer.data)