from django.shortcuts import render, get_list_or_404, get_object_or_404
from .serializers import *
from movies.models import *
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def mypage(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    if request.method == 'GET':
        print(1)
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return Response('회원 탈퇴 되었습니다.')