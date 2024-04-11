from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(max_length=5,primary_key=True)
    FatherName = models.CharField(max_length=15)
    MotherName = models.CharField(max_length=15)
    Address = models.CharField(max_length=50)

    def __str__(self):
        return f"Name : {self.name}"