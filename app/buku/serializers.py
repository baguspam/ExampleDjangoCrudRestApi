from rest_framework import serializers
from . import models

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','kode', 'nama', 'jumlah')
        model = models.Buku

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nim', 'nama', 'email','alamat', 'telepon')
        model = models.Mahasiswa

class PinjamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'tanggal_pinjam', 'kode_buku', 'nim', 'tanggal_kembali', 'denda')
        model = models.Pinjam