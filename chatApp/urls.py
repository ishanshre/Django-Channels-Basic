from django.urls import path
from chatApp import views

app_name = "chatApp"
urlpatterns = [
    path("", views.chat, name="chat"),
]