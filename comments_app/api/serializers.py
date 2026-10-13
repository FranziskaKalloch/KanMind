from rest_framework import serializers

from ..models import Comments


# Serializer für die Ausgabe:
# er liefert id, created_at, author als vollständigen NAmen und content

# Serializer für die Eingabe:
# Er nimmt bei POST nur content entgegen und prüft, ob der Inhalt gültig ist. 


# Für die Ausgabe
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.fullname", read_only=True, allow_null=True) # Der COmmentSerializer bekommt ein Comment. Von diesem Objekt aus sucht er die Felder, die er ausgeben soll. Das Comments Model hat ein Feld namens author, dieses verweist auf den User -> deshalb comments.author.fullname
    class Meta:
        model = Comments
        fields = ('id', 'created_at', 'author', 'content')
        

# POST EINGABE - nur content ist erforderlich
class CommentsCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ('content', )