from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.students)

admin.site.register(models.work)