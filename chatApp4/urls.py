from django.urls import path

from chatApp4 import views

app_name= "chatApp4"
urlpatterns = [
    path("", views.chat4index, name='index')
]