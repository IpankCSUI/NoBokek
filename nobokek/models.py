from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BarangWishlist(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    nama = models.CharField(max_length=150)
    alamat = models.EmailField()
    masalah =models.CharField(max_length=1000)