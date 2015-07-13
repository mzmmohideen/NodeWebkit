from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class TeacherProfile(models.Model):
	staff_name = models.CharField(max_length=100)

class StudentEntries(models.Model):
	user = models.ForeignKey(TeacherProfile)
	student_id = models.CharField(max_length=100)
	student_name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	
# Create your models here.
