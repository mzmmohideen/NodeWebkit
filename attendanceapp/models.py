from django.db import models

class TeacherProfile(models.Model):
	staff_name = models.CharField(max_length=100)

class StudentEntries(models.Model):
	user = models.ForeignKey(TeacherProfile)
	student_name = models.CharField(max_length=100)
	
# Create your models here.
