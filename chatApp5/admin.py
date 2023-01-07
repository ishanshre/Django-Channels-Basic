from django.contrib import admin

# Register your models here.
from chatApp5.models import Chat, Group

admin.site.register(Chat)
admin.site.register(Group)