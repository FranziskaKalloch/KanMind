from django.db import models
from django.conf import settings 
from tasks_app.models import Tasks

# Create your models here.


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name="comments")
    
    class Meta:
        verbose_name = "Comment" #lesbarer Anzeigename für einen einzelnen Eintrag
        
    def __str__(self):
        return f"{self.author} {self.task}"