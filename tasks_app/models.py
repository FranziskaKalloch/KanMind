from django.db import models
from django.conf import settings 
from boards_app.models import Board

# Create your models here.
    
class Tasks(models.Model):
    STATUS_CHOICES = (("TODO", "to-do"), ("INPROGRESS", "in-progress"), ("REVIEW", "review"))
    PRIORITY_CHOICES = (("LOW", "low"), ("MEDIUM", "medium"), ("HIGH", "high"))
    
                       
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="TODO")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=None, null=True, blank=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="review_tasks")
    due_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Task"
        
    def __str__(self):
        return f"{self.board} {self.reviewer}"
    