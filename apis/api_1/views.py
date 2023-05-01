from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import UserModel
from .serializers import UserSerializer



import pandas as pd

class ApiViewSet(viewsets.ModelViewSet):
    
    queryset = UserModel.objects.all()
    

    def get_queryset(self):
        queryset = UserModel.objects.all()
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
    
    def get_serializer_class(self):
        return UserSerializer
    
    def perform_create(self, serializer):
        serializer.save()
    
    #def create(self, request, *args, **kwargs):
    #    
    #    serializer = self.get_serializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    self.perform_create(serializer)
    #    
    #    pk = serializer.data['id']
    #    username = serializer.data['username']
    #    password = serializer.data['password']
    #    return Response(serializer.data)
