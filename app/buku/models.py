from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Buku (models.Model):
    kode = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    class Meta:
       ordering = ["nama"]
    def __str__(self):
        return self.kode

class Mahasiswa (models.Model):
    nim = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    alamat = models.TextField(blank=True)
    telepon = models.CharField(max_length=13)
    class Meta:
       ordering = ["nim"]
    def __str__(self):
        return self.nim

class Pinjam (models.Model):
    kode_buku = models.ForeignKey(Buku, on_delete=models.SET_NULL, null=True)
    nim = models.ForeignKey(Mahasiswa,  on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField(null=True, blank=True)
    denda = models.IntegerField(default=0, null=True, blank=True)
    keterangan = models.TextField(null=True, blank=True)
    class Meta:
       ordering = ["tanggal_pinjam"]