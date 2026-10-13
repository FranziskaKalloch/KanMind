from django.urls import path, include
from .views import AssignToMeView, ReviewingView, CreateTaskView, TaskDetailView


urlpatterns = [
    path("tasks/assigned-to-me/", AssignToMeView.as_view(), name="assigned-to"),
    path("tasks/reviewing/", ReviewingView.as_view(), name="reviewing"),
    path("tasks/", CreateTaskView.as_view(), name="create_task"),
    path("tasks/<int:task_id>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/<int:task_id>/", include("comments_app.api.urls"))
]