from django.contrib import admin
from django.urls import path, include

# ROUTER definieren:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("auth_app.urls"))
]

###### AUFGABEN #####
# Authentication
# Login und Registrierung

# POST /api/registration/
# POST /api/login/

# Boards
# Alles zur Bearbeitung, Erstellung und Abruf von Boards

# GET /api/boards/
# POST /api/boards/
# GET /api/boards/{board_id}/
# PATCH /api/boards/{board_id}/
# DELETE /api/boards/{board_id}/
# GET /api/email-check/

# Tasks
# Alles zur Bearbeitung, Erstellung und Abruf von Tasks

# GET /api/tasks/assigned-to-me/
# GET /api/tasks/reviewing/
# POST /api/tasks/
# PATCH /api/tasks/{task_id}/
# DELETE /api/tasks/{task_id}/
# GET /api/tasks/{task_id}/comments/
# POST /api/tasks/{task_id}/comments/
# DELETE /api/tasks/{task_id}/comments/{comment_id}/#
