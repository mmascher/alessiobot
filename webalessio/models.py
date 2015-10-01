from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    suspend_from = models.DateField(default=None, blank=True, null=True)
    suspend_until = models.DateField(default=None, blank=True, null=True)
    present = models.NullBooleanField()
