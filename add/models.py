from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import datetime

class Money(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    income = models.FloatField()
    outcome = models.FloatField()
    desc_in = models.CharField(max_length=255)
    desc_out = models.CharField(max_length=255)
    date = models.DateField()