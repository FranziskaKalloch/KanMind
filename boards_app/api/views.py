from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import BoardListSerializer
from ..models import Board


# Create your views here.


class BoardListView(generics.ListAPIView): # übernimmt das Abrufen einer Liste
    serializer_class = BoardListSerializer # bestimmt wie ein Board in die JSON Antwort übersetzt wird
    permission_classes = [IsAuthenticated] # nur angemeldete User können zugreifen
    
    def get_queryset(self): # bestimmt, welches Board zurückgegeben wird
        user = self.request.user # ist der Benutzer, der diese Anfrage stellt
        
        boards = Board.objects.filter(Q(owner=user)| Q(members=user)).distinct() # sucht die passenden Boards in der Datenbank, distinct() verhindert doppelte Boards
        return boards
    
  