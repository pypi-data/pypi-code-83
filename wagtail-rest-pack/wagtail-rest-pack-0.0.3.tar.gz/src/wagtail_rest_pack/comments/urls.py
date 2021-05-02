from django.urls import path

from wagtail_rest_pack.comments.create import CreateCommentAPIView
from wagtail_rest_pack.comments.get import ListCommentAPIView
from wagtail_rest_pack.comments.update import DeleteUpdateCommentAPIView

urlpatterns = [
    path('',  ListCommentAPIView.as_view()),
    path('new',  CreateCommentAPIView.as_view()),
    path('<int:pk>', DeleteUpdateCommentAPIView.as_view()),
]