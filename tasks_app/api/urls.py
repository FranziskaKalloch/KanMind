from django.urls import path 
from .views import AssignToMeView


urlpatterns = [
    path("tasks/assigned-to-me/", AssignToMeView.as_view(), name="assigned-to")
]