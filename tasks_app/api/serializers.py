from rest_framework import serializers

from ..models import Tasks
from boards_app.api.serializers import BoardUserSerializer


class TasksSerializer(serializers.ModelSerializer):
    assignee = BoardUserSerializer(read_only=True) # gibt bereits id, email, fullname wieder
    reviewer = BoardUserSerializer(read_only=True)
    comments_count = serializers.SerializerMethodField()
    status = serializers.CharField(source="get_status_display", read_only=True)
    priority = serializers.CharField(source="get_priority_display",read_only=True)
    
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'board', 'description', 'status', 'priority', 'assignee', 'reviewer', 'due_date', 'comments_count')
        
    
    def get_comments_count(self, obj):
        return obj.comments.count() 