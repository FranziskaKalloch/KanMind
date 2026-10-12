from django.urls import path 
from .views import AssignToMeView, ReviewingView, CreateTaskView


urlpatterns = [
    path("tasks/assigned-to-me/", AssignToMeView.as_view(), name="assigned-to"),
    path("tasks/reviewing/", ReviewingView.as_view(), name="reviewing"),
    path("tasks/", CreateTaskView.as_view(), name="create_task")
]