from uuid import uuid4
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

def group_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return '{}.{}'.format(uuid4().hex, ext)

class GroupFile(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    file = models.FileField(upload_to=group_file_name)

    def __str__(self):
        return self.title

