import uuid
import os
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.timezone import now
from users.models import myUser

def user_directory_path(instance, filename):
    unique_id = str(uuid.uuid4())
    ext = filename.split('.')[-1]
    new_filename = f'{unique_id}.{ext}'
    return os.path.join('storage', str(instance.user.id), new_filename)


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    isArchived = models.BooleanField()
    
    def __str__(self) -> str:
        return f'{self.title}'

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phoneNumber = models.CharField(max_length=20)

class EducationalRecord(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    fromDate = models.DateField()
    toDate = models.DateField(validators=[MaxValueValidator(now)])
    user = models.ForeignKey(myUser, on_delete=models.CASCADE, related_name='educational_records')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='educational_records')

class WorkPlace(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phoneNumber = models.CharField(max_length=20)
    expertiseType = models.CharField(max_length=64)

class WorkExperience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    fromDate = models.DateField()
    toDate = models.DateField(validators=[MaxValueValidator(now)])
    user = models.ForeignKey(myUser, on_delete=models.CASCADE, related_name='work_experiences')
    workplace = models.ForeignKey(WorkPlace, on_delete=models.CASCADE, related_name='work_experiences')

class Storage(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=user_directory_path, max_length=2048)
    user = models.ForeignKey(myUser, on_delete=models.CASCADE, related_name='storages')

class AcademicAchievement(models.Model):
    ACHIEVEMENT_TYPE_CHOICES = [
        ('olympiad', 'Olympiad'),
        ('competition', 'Competition'),
        ('top-rating', 'Top Rating'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=12, choices=ACHIEVEMENT_TYPE_CHOICES)
    user = models.ForeignKey(myUser, on_delete=models.CASCADE, related_name='academic_achievements')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='academic_achievements')

class EditRequest(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending for Verify'),
    ]

    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    user = models.ForeignKey(myUser, on_delete=models.CASCADE, related_name='edit_requests')
    fullName = models.CharField(max_length=128, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    bio = models.CharField(max_length=256, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=myUser.GENDER_CHOICES, null=True, blank=True)
