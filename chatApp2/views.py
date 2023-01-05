from django.shortcuts import render

# Create your views here.
def Chat2(request, group_name):
    return render(request, "chat2/chat2.html", {"group_name":group_name})