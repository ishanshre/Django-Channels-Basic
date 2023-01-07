from django.shortcuts import render

from chatApp2.models import Group
# Create your views here.
def Chat2(request, group_name):
    group = Group.objects.filter(name=group_name).first()
    chats=None
    if group:
        chats = group.chats.all()
    else:
        group = Group.objects.create(name=group_name)
        group.save()
    context = {
        "group_name":group_name,
        "chats":chats,
    }
    return render(request, "chat2/chat2.html", context)