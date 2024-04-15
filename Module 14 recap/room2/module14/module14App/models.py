from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)
    father_name = models.CharField(max_length=15)
    # mother_name = models.CharField(max_length=15,default='None'
    
    def __str__(self):
        return f"Name : {self.name}"