from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)
    fathername = models.CharField(max_length=15)
    mothername = models.CharField(max_length=25,default='None')

    def __str__(self):
        return self.name


class student_model(models.Model):
    roll = models.IntegerField(primary_key=True)
    father_name = models.CharField(max_length=15)
    address = models.CharField(20)
