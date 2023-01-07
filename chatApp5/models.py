from django.db import models

# Create your models here.
class Chat(models.Model):
    content = models.CharField(max_length=10000)
    group = models.ForeignKey("Group", on_delete=models.CASCADE, related_name="chats")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"chat of {self.group.name}"

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name