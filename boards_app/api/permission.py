from rest_framework import permissions

from ..models import Board

class IsBoardOwnerOrMember(permissions.BasePermission):
    '''
    Erlaubt den Zugriff nur, wenn der Benutzer der Eigentümer oder ein Mitglied des Boards ist.
    '''
    
    def has_permission(self, request, view): #Diese Prüfung erfolgt vor dem Abrufen des Boards
        return request.user and request.user.is_authenticated # Der Benutzer muss eingeloggt sein
    
    def has_object_permission(self, request, view, obj):
        # 1. Prüfen, ob der Benutzer der Besitzer (Owner) ist
        if request.user == obj.owner:
            return True
        
        # 2. Prüfen, dass nur Owner löschen dürfen
        if request.method == 'DELETE':
            return False
        
        # 3. Prüfen, ob Benutzer ein Member des Boards ist
        if request.user in obj.members.all(): # all() kann nur bei Feldern benutzt werden, die mehrere Objekte zurückgeben, also ein ManyToManyField. Es gibt ein querySet zurück
            return True 
        
        return False 