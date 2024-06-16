from django.db import models

from django.contrib.auth.models import AbstractUser

class myUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=128, null=True)
    age = models.IntegerField(null=True)
    bio = models.CharField(max_length=256, null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    password = models.CharField(max_length=32)
    
    skills = models.ManyToManyField('main.Skill', related_name='users')
