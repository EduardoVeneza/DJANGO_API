from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from trilhas.models import Trail, Step, Link
from .serializers import TrailSerializer, StepSerializer, LinkSerializer


class TrailListAPIView(APIView):

    @swagger_auto_schema(
        responses={200: TrailSerializer(many=True)},
        operation_description="GET /api/trails/ - Retorna uma lista de todas as trilhas cadastradas no banco de dados."
    )
    def get(self, request):
        trails = Trail.objects.all()
        serializer = TrailSerializer(trails, many=True)
        return Response(serializer.data)
    

    @swagger_auto_schema(
        request_body=TrailSerializer,
        responses={201: TrailSerializer},
        operation_description="POST /api/trails/ - Cria uma nova trilha a partir dos dados fornecidos no JSON da requisição."
    )
    def post(self, request, format=None):
        serializer = TrailSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrailDetailAPIView(APIView):

    @swagger_auto_schema(
        responses={200: TrailSerializer},
        operation_description="GET /api/trails/{pk}/ - Retorna os detalhes de uma trilha específica pelo ID."
    )
    def get(self, request, pk):
        trail = get_object_or_404(Trail, id=pk)
        serializer = TrailSerializer(trail)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=TrailSerializer, 
        responses={200: TrailSerializer},
        operation_description="PUT /api/trails/{pk}/ - Atualiza completamente os dados da trilha identificada pelo ID."
    )
    def put(self, request, pk):
        trail = get_object_or_404(Trail, id=pk)
        serializer = TrailSerializer(trail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        request_body=TrailSerializer, 
        responses={200: TrailSerializer},
        operation_description="PATCH /api/trails/{pk}/ - Atualiza parcialmente os dados da trilha pelo ID, permitindo modificar apenas alguns campos."
    )
    def patch(self, request, pk, format=None):
        try:
            trail = Trail.objects.get(pk=pk)
        except Trail.DoesNotExist:
            return Response({"detail": "Trail não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TrailSerializer(trail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={204: 'No Content'},
        operation_description="DELETE /api/trails/{pk}/ - Remove a trilha especificada pelo ID do banco de dados."
    )
    def delete(self, request, pk):
        trail = get_object_or_404(Trail, id=pk)
        trail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StepCreateAPIView(APIView):

    @swagger_auto_schema(
        request_body=StepSerializer,
        responses={201: StepSerializer},
        operation_description="POST /api/trails/{trail_id}/steps/ - Cria um novo step vinculado à trilha especificada."
    )
    def post(self, request, trail_id):
        trail = get_object_or_404(Trail, id=trail_id)
        serializer = StepSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(trail=trail)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StepListCreateForTrail(APIView):
    
    @swagger_auto_schema(
        responses={200: StepSerializer(many=True)},
        operation_description="GET /api/trails/{trail_id}/steps/ - Lista todos os steps da trilha especificada, ordenados pela posição."
    )
    def get(self, request, trail_id):
        steps = Step.objects.filter(trail_id=trail_id).order_by("position")
        serializer = StepSerializer(steps, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=StepSerializer,
        responses={201: StepSerializer},
        operation_description="POST /api/trails/{trail_id}/steps/ - Cria um novo step para a trilha especificada."
    )
    def post(self, request, trail_id):
        trail = get_object_or_404(Trail, id=trail_id)

        data = request.data.copy()  # copia para dict mutável
        data['trail'] = trail.id   # adiciona o ID da trilha no corpo

        serializer = StepSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

    @swagger_auto_schema(
        operation_description="GET /api/steps/{pk}/ - Retorna os detalhes de um step específico pelo ID."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=StepSerializer,
        operation_description="PUT /api/steps/{pk}/ - Atualiza completamente os dados do step identificado pelo ID."
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=StepSerializer,
        operation_description="PATCH /api/steps/{pk}/ - Atualiza parcialmente os dados do step identificado pelo ID."
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="DELETE /api/steps/{pk}/ - Remove o step especificado pelo ID do banco de dados."
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
