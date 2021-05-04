
from django.urls import path

from .view import FormView
from .post import PostFormView

urlpatterns = [
    path('', PostFormView.as_view()),
    path('<str:name>', FormView.as_view()),
]
