from rest_framework import permissions
from django.shortcuts import get_object_or_404
from tasks_app.models import Tasks

class IsTaskBoardMember(permissions.BasePermission):
    '''Erlaubt Zugriff nur für Mitglieder des Boards, zu dem die Task gehört'''
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated: # sicherstellen dass der benutzer eingeloggt ist
            return False
        
        task_id = view.kwargs.get('task_id')
        if not task_id:
            return False
        
        task = get_object_or_404(Tasks, pk=task_id) # Task aus der Datenbank holen
        is_member_of_board = task.board.members.filter(id=request.user.id).exists() # Prüft, ob der User in den Mitgliedern des Boards der Task existiert
        
        return is_member_of_board 