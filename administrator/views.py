from django.shortcuts import render,redirect
from website.models import Custumer, Kategori, Kontak, Profil, Produk, Slide
from cart.models import Transaksi, DetailTransaksi, Produk
# from .forms import KategoriForm, ProdukForm, SlideForm
from django.contrib.auth.decorators import login_required
from website.decorators import ijinkan_pengguna,pilihan_login
from django.db.models import Count, Q, Sum
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

import json

import datetime

from datetime import date
from datetime import datetime
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Alignment



@login_required(login_url='loginpage')
@pilihan_login
def beranda_admin(request):
    jmlKategori = Kategori.objects.filter(aktif=True).count()
    jmlCustumer = Custumer.objects.count()
    jmlProduk = Produk.objects.count()
    jmlTransaksi = Transaksi.objects.filter(status="Lunas").count()
    # grafik = Transaksi.objects.annotate(bulan=Count('date_created__month')).values('bulan')

    # tahun_ini = datetime.now().year
    # bulan_ini = datetime.now().month

    # daftar_bulan = [
    #     {'id': i, 'nama': get_nama_bulan(i)} 
    #     for i in range(1, bulan_ini + 1)
    # ]
   

    # data_transaksi = Transaksi.objects.filter(date_created_year=tahun_ini, date_createdmonth_lte=bulan_ini, status='Lunas')\
    #     .values('date_created__month')\
    #     .annotate(jumlah=Count('id'))
    
    # data_transaksi_per_bulan = [0] * bulan_ini
    # for data in data_transaksi:
    #     bulan = data['date_created__month']
    #     jumlah = data['jumlah']
    #     data_transaksi_per_bulan[bulan-1] = jumlah

    context = {
        'judul': 'Halaman Beranda',
        'menu': 'beranda',
        'jmlKategori':jmlKategori,
        'jmlCustumer':jmlCustumer,
        'jmlproduk':jmlProduk,
        'jmlTransaksi':jmlTransaksi,
        # 'daftar_bulan':json.dumps(daftar_bulan),
        # 'data_transaksi':json.dumps(data_transaksi_per_bulan),
        # 'tahun_ini':tahun_ini,


    }
    return render(request, 'admin_beranda.html', context)