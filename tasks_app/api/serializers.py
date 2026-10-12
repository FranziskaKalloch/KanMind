from rest_framework import serializers

from ..models import Tasks
from auth_app.models import User
from boards_app.api.serializers import BoardUserSerializer

# Ablauf:
# Der TasksSerializer verarbeitet eine Task.
# Bei assignee findet er den zugehörigen Benutzer.
# Er übergibt diesen Benutzer an den BoardUserSerializer.
# Dessen aufbereitete Daten erscheinen als verschachteltes Objekt unter assignee.

# status und priority:
# es wird hier nochmal extra deklariert, weil die Ausgabe sich verändert:
# Ohne eigene Deklaration wird der gespeicherte Wert des Model-Feldes ausgegeben
# Mit source="get_status_display" wird der Anzeigetext der Auswahl ausgegeben

# source= "get_status_display()":
# source sagt dem Serializer: „Hole den Inhalt für dieses Ausgabefeld von dieser anderen Stelle.“
# get_status_display() liefert den Anzeigetext für den aktuell gespeicherten Status einer Task.
# Die Methode kommt von Django. Sobald ein Model-Feld choices besitzt, stellt Django dafür automatische eine Methode bereit:
# get_F00_display()
# Die Methode verändert dabei nichts in der Datenbank. 
# Sie sucht lediglich den passenden Anzeigetext aus den definierten Auswahlmöglichkeiten heraus
# Der name folgt immer diesem Muster: get_ + Feldname + _display()
# source verweist auf diese Methode. Der Serializer ruft sie auf und verwendet den Rückgabewert
class TasksSerializer(serializers.ModelSerializer):
    assignee = BoardUserSerializer(read_only=True) # verschachtelter Serializer. Hier bekommt ein Task eine Beziehung zum Benutzer
    reviewer = BoardUserSerializer(read_only=True)# und es wird id, email, fullname wiedergegeben!
    comments_count = serializers.SerializerMethodField()
    status = serializers.CharField(source="get_status_display", read_only=True)
    priority = serializers.CharField(source="get_priority_display",read_only=True)
    
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'board', 'description', 'status', 'priority', 'assignee', 'reviewer', 'due_date', 'comments_count')
        
    
    def get_comments_count(self, obj):
        return obj.comments.count() 
    
# Für API Reviewing
# Was steht im JSON und was bedeutete es für den Serializer?
# id, title, board, description und due_date müssen ausgegeben werden!
# assignee muss als Objekt mit id, email und fullname ausgegeben werden, dafür wird ein verschachtelter User-Serializer  benötigt
# reviewer mit denselben Benutzerfeldern, da wird dann ebenfalls der user SErializer benötigt
# assiggnee: null -> Ein Task darf keinen zugewiesenen Benutzer haben
# comments_count als Zahl -> diese zahl muss ermittelt werden
# status, priority als Text
# All diese Daten sind bereits im TaskSerializer

###### POST TASKS #####
# bei POST muss der Serializer zurätzlich eingehende Daten annehmen und prüfen

# Der Request liefert einen Text, beispielsweise in-progress.
# Das ChoiceField prüft diesen Text: Ist er unter deinen erlaubten Werten? Falls nein, entsteht ein Validierungsfehler.
# Danach ruft DRF validate_status auf. Die Methode bekommt den erlaubten Text in-progress als value.
# Deine Methode übersetzt ihn in den Model-Wert INPROGRESS und gibt diesen zurück.
# Der zurückgegebene Wert landet in validated_data. Beim späteren Speichern wird dieser verwendet.
class CreateTasksSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=("to-do", "in-progress", "review", "done"))
    priority = serializers.ChoiceField(choices=("low", "medium", "high"))
    assignee_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="assignee", required=False)
    reviewer_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="reviewer", required=False)
    class Meta:
        model = Tasks
        fields = ('board','title', 'description', 'status', 'priority', 'assignee', 'reviewer', 'due_date', 'assignee_id', 'reviewer_id')
    
    # ermittelt den zugehörigen Model-Wert -> bspw: to-do -> TODO
    # DRF ruft sie beim Validieren automatisch auf, weil ihr Name dem Muster validate_ + Feldname entspricht.
    def validate_status(self, value): # Status Umwandlung für das Model # value enthält den bereits geprüften Statuswert
        if value == "to-do": # ist der Inhalt von value gleich dem TExt "to-do"
            return "TODO"
        elif value == "in-progress":
            return "INPROGRESS"
        elif value == "review":
            return "REVIEW"
        elif value == "done":
            return "DONE"
    
    # dient nur der Felder Validierung, also eines Felds!   
    def validate_priority(self, value):
        if value == "low":
            return "LOW"
        elif value == "medium":
            return "MEDIUM"
        elif value == "high":
            return "HIGH"
     
     
    # dient der feldübergreifenden Validierung
    # attrs: Ein Dictionary (Wörterbuch), das alle bereits vorvalidierten Werte der Serializer-Felder enthält.
    # in attrs findet man die Werte über ihre Schlüssel: board, assignee, reviewer, title
    def validate(self, attrs):
        # 1. Werte aus dem attrs-Dictonary auslesen - das Board holen und die Tasks
        board = attrs.get('board')
        assignee = attrs.get('assignee')
        reviewer = attrs.get('reviewer')
        
        if assignee is not None:
            if not board.members.filter(id=assignee.id).exists():
                raise serializers.ValidationError("The assignee must be a member of the board.")
        
        if reviewer is not None:
            if not board.members.filter(id=reviewer.id).exists():
                raise serializers.ValidationError("The Reviewer must be member of the board")
            
        return attrs
                

# PrimaryKeyRelatedField()
# Primary Key = ID des Nutzers
# Related bedeutet, dass es um eine Beziehung zu einem anderen Model geht
# Field bedeutet Serializer Feld
# Zusammen: Ein Serializer-Feld, das eine Beziehung anhand einer ID verarbeitet.
# Das queryset ist dabei die Vorgabe: „In dieser Menge von Benutzern darfst du suchen.“
# queryset: Sucht den Benutzer anhand der übermittelten ID.
#source="assignee": Ordnet das gefundene Benutzerobjekt dem Model-Feld assignee zu.
#required=False: Das Eingabefeld darf fehlen.