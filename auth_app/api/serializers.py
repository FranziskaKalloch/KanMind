from django.contrib.auth import authenticate
from rest_framework import serializers
from auth_app.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Hier werden neue Felder angelegt, da die im Model nicht vorkommen
    password = serializers.CharField(write_only=True) # Felddefinition: hiermit wird beschrieben "Mein Serializer hat ein Textfeld namens password, das nur als Eingabe verwendet werden darf"
    repeated_password = serializers.CharField(write_only=True)    
    class Meta:
        model = User
        fields = ("fullname", "email", "password", "repeated_password")
        
    # prüft: stimmen die Passwörter überein, wenn nicht, dann wird ein Validierungs-
    # fehler geraist. Stimmen sie überein, werden die geprüften Daten zurück gegeben.
    # hier -> Validierung auf Objektebene (mehrere Felder verlgeichchen)
    # dazu wird er Parameter 'data' genutzt
    def validate(self, data):
        password = data['password']
        repeated_password = data['repeated_password']
                
        if password != repeated_password:
            raise serializers.ValidationError("password dont match")
        return data
    
    # speichert E-Mail, vollständigen Namen und das gehashte Passwort. 
    # Die E-Mail wird zusätzlich als interner Benutzername verwendet
    def create(self, validated_data): # create_user wird genutzt, damit das Passwort sicher gehasht wird
        user = User.objects.create_user(
            username=validated_data['email'], 
            email=validated_data['email'], 
            password=validated_data['password'],
            fullname=validated_data['fullname']) #creates, saves and returns a User
        return user
    # mit validated_data übergibt man die tatsächlich geprüften Eingaben. 
    
    class UserLoginSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField(write_only=True)
        
        def validate(self, data):
            email = data['email']
            password = data['password']
            
            user = authenticate(username=email, password=password)
            
            if not user:
                raise serializers.ValidationError("User not found")
            
            data['user'] = user
            return data 