from django.shortcuts import render

# Create your views here.

def chat4index(request):
    return render(request, "chat4/index.html")