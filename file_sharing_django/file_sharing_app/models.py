from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    members = models.ManyToManyField(User, related_name="members", through='GroupMembership', blank=True)
    name = models.CharField(max_length=200)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GroupMembership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")
    date_joined = models.DateTimeField(auto_now_add=True)

