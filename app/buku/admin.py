from django.contrib import admin
from .models import *

# Register your models here.
class BukuAdmin (admin.ModelAdmin):
    list_display = ['kode', 'nama', 'jumlah']
    list_filter = ()
    search_fields = ['kode', 'nama']
    list_per_page = 25
    pass
admin.site.register(Buku, BukuAdmin)

class MahasiswaAdmin (admin.ModelAdmin):
    list_display = ['nim', 'nama', 'email','alamat', 'telepon']
    list_filter = ()
    search_fields = ['nim', 'nama', 'email', 'alamat', 'telepon']
    list_per_page = 25
    pass
admin.site.register(Mahasiswa, MahasiswaAdmin)

class PinjamAdmin (admin.ModelAdmin):
    list_display = ['tanggal_pinjam', 'kode_buku', 'nim', 'tanggal_kembali', 'denda', 'keterangan']
    list_filter = ()
    search_fields = ['tanggal_pinjam', 'kode_buku', 'nim', 'tanggal_kembali', 'keterangan']
    list_per_page = 25
    pass
admin.site.register(Pinjam, PinjamAdmin)