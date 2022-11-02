from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class PendapatForum(models.Model):
    nama = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    angkatan = models.CharField(max_length=100)
    pendapat = models.TextField()
