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
