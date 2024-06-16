from django.db import models

from django.contrib.auth.models import AbstractUser

class myUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=128)
    age = models.IntegerField()
    bio = models.CharField(max_length=256)
    birthDate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    password = models.CharField(max_length=32)
