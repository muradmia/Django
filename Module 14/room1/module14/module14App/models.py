from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField(max_length=20)
    father_name = models.CharField(max_length=20,default="Murad")

    def __str__(self):
        return f"Name : {self.name}"


class work(models.Model):
    name = models.CharField(max_length=15)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField(max_length=20)