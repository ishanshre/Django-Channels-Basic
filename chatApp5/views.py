from django.shortcuts import render
from chatApp5.models import Group
# Create your views here.
def chat5index(request, groupName):
    group = Group.objects.filter(name=groupName).first()
    chats = None
    if group:
        chats = group.chats.all()
    else:
        group = Group.objects.create(name=groupName)
        group.save()
    
    context = {
        'groupName':groupName,
        'chats':chats
    }
    return render(request, "chat5/index.html", context)