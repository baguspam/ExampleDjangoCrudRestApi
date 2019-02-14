from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class BukuList(generics.ListCreateAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

    def get_read_serializer_class(self):
        if self.request.method == 'POST':
            return BukuSerializer
        return BukuSerializer

class BukuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class MahasiswaList(generics.ListCreateAPIView):
    queryset =  Mahasiswa.objects.all()
    serializer_class =  MahasiswaSerializer

    def get_read_serializer_class(self):
        if self.request.method == 'POST':
            return  MahasiswaSerializer
        return  MahasiswaSerializer

class  MahasiswaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Mahasiswa.objects.all()
    serializer_class =  MahasiswaSerializer


class PinjamList(generics.ListCreateAPIView):
    queryset = Pinjam.objects.all()
    serializer_class = PinjamSerializer

    def get_read_serializer_class(self):
        if self.request.method == 'POST':
            return PinjamSerializer
        return PinjamSerializer

class PinjamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pinjam.objects.all()
    serializer_class = PinjamSerializer