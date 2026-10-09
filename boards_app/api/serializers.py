from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Board
from tasks_app.models import Tasks

class BoardListSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField() # SerializerMethodField ist eine Ausgabefeld, dessen Wert du mit einer Methode berechnest
    ticket_count = serializers.SerializerMethodField() # es sagt DRF: Für dieses Feld ruf meine Methode auf!
    tasks_to_do_count = serializers.SerializerMethodField()
    tasks_high_prio_count = serializers.SerializerMethodField()
    
    def get_member_count(self, obj): # obj ist bereits das aktuell Board
        return obj.members.count() # zählt die Mitglieder des Boards
    
    def get_ticket_count(self, obj):
        return obj.tasks.count() # zählt alle tasks, wird über related_name="tasks" erreicht
    
    def get_tasks_to_do_count(self, obj):
        return obj.tasks.filter(status="TODO").count() # 
    
    def get_tasks_high_prio_count(self, obj):
        return obj.tasks.filter(priority="HIGH").count() #obj.tasks-> greift auf die Tasks dieses Board zu. Das wird durch related_name="tasks" im Task Model ermöglicht
    
    class Meta:
        model = Board
        fields = ('id', 'title', 'owner_id', 'member_count', 'ticket_count', 'tasks_to_do_count', 'tasks_high_prio_count')

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('title', 'members')
        

class BoardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model() # liefert das User Model zurück
        fields = ('id', 'email', 'fullname')
        
    
class BoardTaskSerializer(serializers.ModelSerializer):
    assignee = BoardUserSerializer(read_only=True)
    reviewer = BoardUserSerializer(read_only=True)
    comments_count = serializers.SerializerMethodField()
    status = serializers.CharField(source="get_status_display", read_only=True) # get_status_display holt aus dem choices den Rückgabewert. Gespeichert ist "TODO" -> zurückgegeben wird "to-do"
    priority = serializers.CharField(source="get_priority_display", read_only=True) # source sagt dem Serializer, woher der Wert für das Ausgabefeld kommen soll. Ohne source nimmt das Feld status automatisch den Wert aus task.status → "TODO". Mit source="get_status_display" nimmt es stattdessen das Ergebnis von task.get_status_display() → "to-do".
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'status', 'priority', 'due_date', 'assignee', 'reviewer', 'comments_count')
    def get_comments_count(self, obj):
        return obj.comments.count() 
      
class BoardDetailSerializer(serializers.ModelSerializer):
    members = BoardUserSerializer(many=True, read_only=True)
    tasks = BoardTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = ('id', 'title', 'owner_id', 'members', 'tasks')
        

# Dieser serializer bereitet ausschließlich die Antwort vor für PATCH
class BoardUpdateResponseSerializer(serializers.ModelSerializer):
    owner_data = BoardUserSerializer(source="owner", read_only=True) # die Daten kommen aus der Board-Beziehung owner
    members_data = BoardUserSerializer(source="members", many=True, read_only=True)
    class Meta:
        model = Board
        fields = ('id', 'title', 'owner_data', 'members_data')

