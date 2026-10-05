from rest_framework import serializers
from auth_app.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("fullname", "email", "password", "repeated_password")
        
    # Daten prüfen
    # validate()
    def validate(self):
        pass
        
    # Benutzer erstellen
        
    def create(self):
        pass
    #Benutzer sicher mit gehashtem Passwort anlegen