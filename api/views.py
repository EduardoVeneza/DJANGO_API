from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from trilhas.models import Trail
from .serializers import TrailSerializer

class TrailListAPIView(APIView):

    @swagger_auto_schema(responses={200: TrailSerializer(many=True)}, operation_description="Retorna Tudo")
    def get(self, request):
        trails = Trail.objects.all()
        serializer = TrailSerializer(trails, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
        request_body=TrailSerializer,
        responses={201: TrailSerializer}
    )
    def post(self, request, format=None):
        serializer = TrailSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrailDetailAPIView(APIView):

    @swagger_auto_schema(responses={200: TrailSerializer})
    def get(self, request, pk):
        trail = get_object_or_404(Trail, id=pk)
        serializer = TrailSerializer(trail)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TrailSerializer, responses={200: TrailSerializer})
    def put(self, request, pk):
        trail = get_object_or_404(Trail, id=pk)
        serializer = TrailSerializer(trail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        trail = get_object_or_404(Trail, id=pk)
        trail.delete()
        return Response(status=status.HTTP_200_OK)


# class TrailCreateAPIView(APIView):

#     @swagger_auto_schema(
#         request_body=TrailSerializer,
#         responses={201: TrailSerializer}
#     )
#     def post(self, request, format=None):
#         serializer = TrailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
