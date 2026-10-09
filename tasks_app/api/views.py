from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Tasks 
from .serializers import TasksSerializer


class AssignToMeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        tasks = Tasks.objects.filter(assignee=user)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)
        
        # Angemeldeten User ermitteln — über request.user.
        # Seine Tasks suchen — Tasks, deren assignee dieser User ist.
        # Tasks aufbereiten — einen Serializer verwenden, mit many=True, weil mehrere Tasks zurückkommen können.
        # Antwort zurückgeben — die aufbereiteten Daten als Response