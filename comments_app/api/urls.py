from django.urls import path
from .views import CommentsView


urlpatterns = [
  path("comments/", CommentsView.as_view(), name="comments"),
  path("comments/<int:comment_id>/",)
]