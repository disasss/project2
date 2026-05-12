from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)

class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)   # имя
    last_name = models.CharField(max_length=100)    # фамилия
    age = models.IntegerField()                     # возраст
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    clubs = models.ManyToManyField(Club, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"