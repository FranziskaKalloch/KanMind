"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# ROUTER definieren:


urlpatterns = [
    path('admin/', admin.site.urls),
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
