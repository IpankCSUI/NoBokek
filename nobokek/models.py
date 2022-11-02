from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BarangWishlist(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()