from django.urls import path

from chatApp2 import views
app_name = "chatApp2"
urlpatterns = [
    path("<str:group_name>/", views.Chat2, name="Chat2")
]