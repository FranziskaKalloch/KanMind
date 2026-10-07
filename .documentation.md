from django.db import models
from django.contrib.auth.models import AbstractUser
'''
Für Aufgabe 1 - POST /api/registration/
Djangos Benutzermodell: Wo werden Benutzer gespeichert, und wie werden sie mit sicherem Passwort erstellt?
DRF-Serializer: Wie werden die eingehenden Felder geprüft?
DRF-Token-Authentifizierung: Wie wird ein Token erstellt und später verwendet?
'''

# DJANGO BENUTZERMODELL:
# AbstractUser als Benutzermodell erlaubt es eigene Felder hinzuzufügen
# wie in diesem Beispiel: fullname als eigenes Feld.
# AbustracUser ist eine Vorlage von Django, genau wie User, die bereits alle Felder und Methoden enthält, die ein Benutzer benötigt.

# AUTH_USER_MODEL
# In settings.py kann das Benutzermodell angepasst werden:
# AUTH_USER_MODEL = 'auth_app.User'
# Damit wird Django gesagt, dass das eigene User-Modell verwendet werden soll,
# anstatt des Standardmodells. Ohne diese Einstellung würde Django das Standardmodell verwenden,
# das nicht die zusätzlichen Felder enthält.

# DAS ABSTRACTUSER-MODELL:
# ebenfalls enthalten

class AbstractUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField()
    user_permissions = models.ManyToManyField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
'''
Anmeldung 

POST /api/registration
'''
# Erstellt einen neuen Benutzer
# Token-basierte session
# Der Request Body sollte so aussehen:
# {
#    "fullname": "Franziska Kalloch",
#    "email": "f.kalloch@outlook.de",
#    "passwort": "blabla",
#    "repeated_password": "blabla"
# }

## Schritte Registration:
# 1. Model vorbereiten: Wo werden Name, E-Mail und Passwort-Hash gespeichert?
# 2. Serializer erstellen: Sind die Angaben gültig, stimmen die Passwörter überein und
# .. ist die E-Mail noch frei? Anschließend wird der Benutzer mit gehashtem Passwort angelegt
# 3. View erstellen: Sie nimmt die Anfrage entgegen, verwendet den Serializer und gibt Token sowie
# ... Benutzerinformationen zurüc
# 4. URL verbinden: Die Registrierung wird unter /api/registration/ erreichbar
# 5. Mit Postman prüfen: Erfolgreiche REgistrierung ergibt 201, fehlerhafte ergeben 400


'''
Board Model
'''
# BOARD - die Sammlung von Aufgaben
# Name des Boards
# Owner des Boards, verweist auf den Benutzer, der das Board erstellt hat
# Members, Benutzer die am Board mitarbeiten

### Beziehungen 
# Ein Benutzer kann mehrere Boards haben, jedes Board hat nur einen OWNER! OneToMany
# Ein Board kann mehrere Mitglieder haben, ein Benutzer kann Mitglied mehrere Boards sein - ManyToMany

'''
Task Model
'''
## TASKS - Aufgaben innerhalb eines Boards
# board, zu dem die Aufgabe gehört
# title - Titel der Aufgabe
# description - genauere Beschreibung der Aufgabe
# status - Bearbeitungszustand
# priority - WIchtigkeit
# assignee - Benutzer, der die Aufgabe bearbeitet
# reviewer - Benutzer, der das Ergebnis prüft
# due_date - Fälligkeitsdatum
# created_at - Wann wurde die Aufgabe erstellt

## Beziehungen
# Ein Board hat mehrere Aufgaben, eine Aufgabe gehört nur zu einem Board -> OneToMany!

'''
Comment Model
'''
## Comment - eine Nachricht zu einer Aufgabe
# task, die Aufgabe, zu der der Kommentar gehört (Beziehungsfeld)
# author, Benutzer, der den Kommentar geschrieben hat (Beziehungsfeld zum User)
# content, Kommentartext
# created_at - Erstellungszeitpunkt

## Beziehungen
# Eine Aufgabe kann mehrere Kommentare haben. 
# Jeder Kommentar gehört zu einer Aufgabe und hat nur einen Autor!