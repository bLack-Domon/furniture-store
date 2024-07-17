from django.contrib import admin
from django.db import models
from django.forms import TextInput
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis,ChatID, Custumer

class DataKategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif","banner_satu","banner_dua",) 
    prepopulated_fields = {"slug": ("nama",)}

class DataProdukAdmin(admin.ModelAdmin):
    list_display = ("nama_produk", "gambar", "kategori", "harga","no_whatsup",)
    prepopulated_fields = {"slug": ("nama_produk",)}

class DataKontak(admin.ModelAdmin):
    list_display = ("nama", "email", "telpon", "subjek")

admin.site.register(Kategori, DataKategoriAdmin)
admin.site.register(Produk, DataProdukAdmin)
admin.site.register(Slide)
admin.site.register(Kontak, DataKontak)
admin.site.register(Profil)
admin.site.register(Statis)
admin.site.register(ChatID)
admin.site.register(Custumer)
