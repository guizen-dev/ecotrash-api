from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

# Create your views here.


@api_view(['GET', 'POST'])
def all_users_endpoint(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def specific_recycle_endpoint(request, user_id):
    
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'message' : 'O usuario nao existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)
    
    if request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message' : 'Usuario deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)