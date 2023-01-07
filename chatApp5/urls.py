from django.urls import path
from chatApp5 import views

app_name="chatApp5"


urlpatterns = [
    path('<str:groupName>/', views.chat5index, name='index'),
]