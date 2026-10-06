from django.db import models
from django.conf import settings # für eine saubere Verknüpfung von Models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_boards")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="member_boards")