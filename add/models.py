from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import datetime

class Money(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    income = models.FloatField(null=True, blank=True)
    outcome = models.FloatField(null=True, blank=True)
    desc_in = models.CharField(max_length=255,null=True, blank=True)
    desc_out = models.CharField(max_length=255,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    note = models.CharField(max_length=255,null=True, blank=True)
    