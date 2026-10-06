from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import BoardListSerializer
from ..models import Board


# Create your views here.


class BoardListView(generics.ListAPIView):
    serializer_class = BoardListSerializer
    permission_classes = [IsAuthenticated] # nur angemeldete User können zugreifen
    
    def get_queryset(self):
        user = self.request.user
        
        boards = Board.objects.filter(Q(owner=user)| Q(members=user)).distinct()
        return boards
    
  