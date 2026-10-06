from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import Response 

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
    def post(self, request):
        return Response('ich bin eine APIView')
        


# Create your views here.



# Die Registrierungs-View steuert den Ablauf der Anfrage. 
# Dein Serializer übernimmt dabei weiterhin die Prüfung und Benutzererstellung.

# POST-Anfrage entgegennehmen.
# Registrierung muss ohne Anmeldung erlaubt sein.

# Die Eingaben an deinen Serializer übergeben.
# Die gesendeten Werte findest du in request.data.

# Den Serializer validieren lassen.
# Bei ungültigen Daten soll eine Antwort mit Status 400 entstehen.

# Den Benutzer speichern lassen.
# Die View ruft dafür save() am Serializer auf. DRF führt dann deine create()-Methode aus und liefert den Benutzer zurück.

# Ein Token für den Benutzer erstellen.

# Die Antwort zurückgeben.
# Sie enthält token, fullname, email und user_id sowie den Status 201.





# POST /api/registration/

# Description: Erstellt einen neuen Benutzer.
# Request Body
# {
#  "fullname": "Example Username",
# "email": "example@mail.de",
#  "password": "examplePassword",
#  "repeated_password": "examplePassword"
# }
# Success Response
# Erfolgreicher Erstellung gibt dies ein Token sowie die Benutzerinformationen zurück, inklusive die einzigartige Nutzer-ID.
# {
#  "token": "83bf098723b08f7b23429u0fv8274",
#  "fullname": "Example Username",
#  "email": "example@mail.de",
#  "user_id": 123
# }
# Status Codes
# 201: Der Benutzer wurde erfolgreich erstellt.
# 400: Ungültige Anfragedaten.
# 500: Interner Serverfehler.
# Rate Limits
# No limit
# No Permissions required
