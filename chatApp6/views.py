from django.shortcuts import render

from chatApp6.models import Group

# Create your views here.
def chat6Index(request, groupName):
    group = Group.objects.filter(name=groupName).first()
    chats = None
    if group:
        group = Group.objects.get(name=groupName)
        chats = group.chats.all()
    else:
        group = Group.objects.create(name=groupName)
    context = {
        "groupName":groupName,
        "chats":chats
    }
    return render(request, "chat6/index.html", context)