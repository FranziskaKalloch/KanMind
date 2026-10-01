from django.shortcuts import render

# Create your views here.


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
