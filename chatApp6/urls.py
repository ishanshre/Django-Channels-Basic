from django.urls import path
from chatApp6 import views

app_name = "chatApp6"
urlpatterns = [
    path("<str:groupName>/", views.chat6Index, name="index"),
    path("message/outside/", views.sendMsgFromOutside, name='message')
]