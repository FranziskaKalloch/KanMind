from rest_framework import serializers

from ..models import Board

class BoardListSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    
    def get_member_count(self, obj):
        return obj.members.count()
    class Meta:
        model = Board
        fields = ('id', 'title', 'owner_id', 'member_count')
        