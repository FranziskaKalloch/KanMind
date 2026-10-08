from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Board, Tasks

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
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'status', 'priority', 'due_date', 'assignee', 'reviewer', 'comments_count', 'tasks')
    def get_comments_count(self, obj):
        return obj.comments.count()   
class BoardDetailSerializer(serializers.ModelSerializer):
    members = BoardUserSerializer(many=True, read_only=True)
    tasks = BoardTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = ('id', 'title', 'owner_id', 'members')
    # GET-Antwort: Board-Felder, Mitglieder und Tasks zusammenführen

