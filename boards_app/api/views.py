from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import BoardListSerializer, BoardCreateSerializer, BoardDetailSerializer, BoardUpdateResponseSerializer
from ..models import Board
from .permission import IsBoardOwnerOrMember

class BoardListView(generics.ListCreateAPIView): # übernimmt das Abrufen einer Liste
    serializer_class = BoardCreateSerializer # bestimmt wie ein Board in die JSON Antwort übersetzt wird
    permission_classes = [IsAuthenticated] # nur angemeldete User können zugreifen
    
    def get_queryset(self): # bestimmt, welches Board zurückgegeben wird
        user = self.request.user # ist der Benutzer, der diese Anfrage stellt
        
        boards = Board.objects.filter(Q(owner=user)| Q(members=user)).distinct() # sucht die passenden Boards in der Datenbank, distinct() verhindert doppelte Boards
        return boards
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return BoardCreateSerializer
        else:
            return BoardListSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
    def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       self.perform_create(serializer)
       response_serializer = BoardListSerializer(serializer.instance)
       return Response(response_serializer.data, status=status.HTTP_201_CREATED)
  
  
# Diese View kombiniert Details (GET), Updates (PUT/PATCH), und LÖSCHEN (DELETE) 
# Diese View kann jetzt automatisch GET, PUT, PATCH und DELETE per ID    
class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    
    # Der User muss eingeloggt sein UND die Board-Bedingung erfüllen
    permission_classes = [IsAuthenticated, IsBoardOwnerOrMember]
    
    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return BoardCreateSerializer
        return BoardDetailSerializer
    
    def update(self, request, *args, **kwargs):
        board = self.get_object() # einzelnes Board holen, anhand der ID
        serializer = self.get_serializer(board, data=request.data, partial=True) # Das Board wird übergeben, so wie die Daten aus dem Serializer
        serializer.is_valid(raise_exception=True)
        serializer.save() # Hier wird das Board aktualisiert
        response_serializer = BoardUpdateResponseSerializer(serializer.instance)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    
    
    #### Die View kümmert sich darum:
    # Welches Board ist gemeint?
    # Darf der Benutzer darauf zugreifen?
    # Soll es gelesen, geändert oder gelöscht werden?
    
    ### Nachdem die View das Board gefunden hat, kümmert sich der Serializer darum:
    # Welche Informationen kommen in die Antwort?
    # Wie werden Mitglieder und Tasks dargestellt?
    # Welcher Text soll bei status erscheinen?