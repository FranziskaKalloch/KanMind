from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks_app.models import Tasks
from .serializers import CommentSerializer, CommentsCreateSerializer
from .permission import IsTaskBoardMember, IsAuthor
from ..models import Comments


class CommentsView(APIView):
    permission_classes = [IsAuthenticated, IsTaskBoardMember]
    
    def get_task(self, task_id):
        '''Hilfsmethode, um das Objekt (hier den Task) zu holen oder einen 404 Fehler zu werfen'''
        return get_object_or_404(Tasks, pk=task_id) # pk ist die ID in der Datenbank, task_id der Parametername in der URL
        
    
    def get(self, request, task_id):
        '''Lädt und gibt das Objekt anhand der ID zurück'''
        task = self.get_task(task_id)  # die Methode get_task wird aufgerufen und in der Variablen Task gespeichert
        serializer = CommentSerializer(task.comments.all().order_by("created_at"), many=True) # lädt alle Kommentare und sortiert die ältesten zuerst
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, task_id):
        '''Erstellt einen neuen Kommentar zur Task'''
        task = self.get_task(task_id) # Objekt wird anhand der ID geholt
        serializer = CommentsCreateSerializer(data=request.data) # Daten an den Serializer übergebe. 
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save(task=task, author=request.user)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]
    
    def get_comment(self, task_id, comment_id):
        '''Lädt und gibt den Kommentar anhand der ID zurück'''
        return get_object_or_404(Comments, task_id=task_id, pk=comment_id)
    
    def delete(self, request, task_id, comment_id):
        comment = self.get_comment(task_id, comment_id)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)