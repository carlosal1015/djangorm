#!/bin/python3
from django.db import models


# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default="")


try:
    alice = User.objects.get(name="Alice")
except:
    alice = User(name="Alice")
    alice.save()

for user in User.objects.all():
    print(f"ID: {user.id}\tUsername: {user.name}")
