from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, UserLoginSerializer

# APIView:
# man kann mit der APIView selbst bestimmen, was bei GET, POST und anderen
# HTTP Methoden passiert.

# Generische Views:
# Vorgefertigte Abläufe, bspw. Datensätze auflisten oder einen Datensatz erstellen
# Man ergänzt vor allem model und Serializer

# ViewSets:
# Bündelt mehrere Aktionen für eine Ressource, etwa Aufgaben auflisten,
# erstellen, bearbeiten und löschen. Ein Router kann die URL's zuordnen
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request): #request enthält die eingehende Anfrage | über request.data kommt man später an alle Registrierungsdaten
        serializer = UserRegistrationSerializer(data=request.data) # Hier muss eine Instanz erstellt werden (). # Die Anfragedaten werden an den Parameter data des Serializers übergeben.
        serializer.is_valid(raise_exception=True) # Jetzt müssen die Eingaben vom Serializer geprüft werden, dafür wird die is_valid() Methode benutzt
        user = serializer.save() # Hiermit wird der User erstellt, mit save() führt DRF eine create() Methode im Serializer aus und gibt einen gespeicherten Nutzer zurück. Das wird in der Variable user gespeichert, damit kann dann später der Token erstellt werden

        # Token generieren
        token, created = Token.objects.get_or_create(user=user) # token enthält das Token-Objekt. Created sagt, ob es neu erstellt wurde oder bereits vorhanden ist
        
        return Response({
            "token": token.key,
            "fullname": user.fullname,
            "email": user.email,
            "user_id": user.id
        }, status=status.HTTP_201_CREATED) 
        # es wird hier ein dictonary übergeben, weil die Antwort mehrere Werte enthalten soll!

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        
        token, create = Token.objects.get_or_create(user=user)
        
        return Response({
                    "token": token.key,
                    "fullname": user.fullname,
                    "email": user.email,
                    "user_id": user.id
                }, status=status.HTTP_200_OK)