from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)
    mother = models.CharField(max_length=20)
    father = models.CharField(max_length=15,default="monir")


    def __str__(self):
        return self.name

class student(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)
    fathername = models.CharField(max_length=15)
    address = models.CharField(max_length=15)

    def __str__(self):
        return f"Name : {self.name}" 
    