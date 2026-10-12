from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import status

from django.shortcuts import get_object_or_404

from ..models import Tasks 
from .serializers import TasksSerializer, CreateTasksSerializer, UpdateSerializer, TaskUpdateResponseSerializer


class AssignToMeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        tasks = Tasks.objects.filter(assignee=user)
        serializer = TasksSerializer(tasks, many=True) # der Serializer muss wissen, welche Daten er aufbereiten soll, daher tasks. Tasks enthält die gefundenen Tasks des angemeldeten users
        return Response(serializer.data)
        # Angemeldeten User ermitteln — über request.user.
        # Seine Tasks suchen — Tasks, deren assignee dieser User ist.
        # Tasks aufbereiten — einen Serializer verwenden, mit many=True, weil mehrere Tasks zurückkommen können.
        # Antwort zurückgeben — die aufbereiteten Daten als Response
        
class ReviewingView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user # Benutzer wird ermittelt.
        tasks = Tasks.objects.filter(reviewer=user) # Finde alle Tasks, deren Reviewer dieser Benutzer ist., reviewer das Modelfeld, das geprüft werden soll # user: das Benutzerobjekt, mit dem verglichen werden soll
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)
        
# In der JSON Response ist eine [], dass heisst: es kommt eine liste zurück. Daher
# wird für den Serializer Aufruf in der View ein many=True benötigt. 
# serializer = TasksSerializer(many=True)
# Tasks, bei denen der aktuell authentifizierte Benutzer als Reviewer eingetragen ist.
# Daraus ergeben sich folgende Aufgaben:
# Anmeldung verlangen
# Den angemeldeten Benutzer ermitteln
# Tasks suchen, deren Reviewer dieser Benutzer ist
# Die gefundenen Tasks mit den vorhandenen Serializer als Liste aufbereiten
# Die Daten zurück geben
    
# Was ist request?
# Wenn jemand deinen Endpunkt aufruft, erhält deine View ein Request-Objekt. 
# Es enthält Informationen über die eingehende Anfrage, beispielsweise:
# die HTTP-Methode, etwas GET
# übermittelte Daten,
# INformationen zur Authentifizerung
# Bei einer APIView stellt Django REST Framework dieses Objekt bereit und übergibt es deiner get-Methode

# Was ist request.user?
# Die konfigurierte Authentifizierung ermittelt, welcher Benutzer die Anfrage stellt. 
# Diesen Benutzer erreichst du über die Eigenschaft user des Request-Objekts

class CreateTaskView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # die EingabeDaten an den Serializer übergeben
        serializer = CreateTasksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # die Daten validieren
        board = serializer.validated_data.get('board') # das Board Objekt holen
        if not board.members.filter(id=request.user.id).exists():
            raise PermissionDenied
        task = serializer.save() # erstellt die Task aus den geprüften Daten und gibt das neu erstellte Task Objekt zurück
        serializer = TasksSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    class TaskDetailView(APIView):
        permission_classes = [IsAuthenticated]
        
        def patch(self, request, task_id):
            '''
            Task aktualisieren
            '''
            task = get_object_or_404(Tasks, id=task_id) # gesucht wird im Model Tasks
            board = task.board # Das Board des Task
            
            if not board.members.filter(id=request.user.id).exists(): # nur boardmember dürfen danach weitermachen
                raise PermissionDenied
            
            # jetzt wird der Eingabe Serializer benötigt
            serializer = UpdateSerializer(task, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            serializer = TaskUpdateResponseSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def delete(self, request, task_id):
            pass