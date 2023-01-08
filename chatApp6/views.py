from django.shortcuts import render, HttpResponse

from chatApp6.models import Group

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

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


def sendMsgFromOutside(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "hello",
        {
            "type":"chat.message",
            "message":"Message from outside the consiumer"
        }
    )
    return HttpResponse("Message from Outside")