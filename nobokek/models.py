from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    nama = models.TextField(null=True, blank=True)
    alamat = models.TextField(null=True, blank=True)
    masalah =models.TextField(null=True, blank=True)
