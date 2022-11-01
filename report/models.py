from django.db import models

from django.contrib.auth.models import User
import datetime
from add.models import Money

# Create your models here.

class ReportUser(models.Model):
    # userAdd = models.ForeignKey(Money, on_delete=models.PROTECT, unique=True, null=True)
    userAdd = models.ManyToManyField(Money, blank=True)


class Pesan(models.Model):
    nama = models.CharField(max_length=15)
    isi = models.TextField(max_length=150)

    def __str__(self):
        return self.nama

# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()


