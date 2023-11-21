from .models import Recycle
from .serializers import RecycleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
def all_recycling_endpoint(request):
    if request.method == 'GET':
        recycle = Recycle.objects.all()
        recycle_serializer = RecycleSerializer(recycle, many=True)
        return JsonResponse(recycle_serializer.data, safe=False)
    
    elif request.method == 'POST':
        recycle_serializer = RecycleSerializer(data=request.data)
        if recycle_serializer.is_valid():
            recycle_serializer.save()
            return JsonResponse(recycle_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(recycle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def specific_user_endpoint(request, recycle_id):
    
    try:
        recycle = Recycle.objects.get(pk=recycle_id)
    except Recycle.DoesNotExist:
        return JsonResponse({'message' : 'A reciclagem nao existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        recycle_serializer = RecycleSerializer(recycle)
        return JsonResponse(recycle_serializer.data)
    
    if request.method == 'PUT':
        recycle_data = JSONParser().parse(request)
        recycle_serializer = RecycleSerializer(recycle, data=recycle_data)
        if recycle_serializer.is_valid():
            recycle_serializer.save()
            return JsonResponse(recycle_serializer.data)
        return JsonResponse(recycle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        recycle.delete()
        return JsonResponse({'message' : 'Reciclagem deletada com sucesso!'}, status=status.HTTP_204_NO_CONTENT)