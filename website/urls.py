from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutpage, name='logoutpage'),
    path('', views.beranda, name='beranda'),
    path('profil-kami', views.profil, name='profil'),
    path('<slug:kategori_slug>/<slug:slug>', views.produk, name='produk'),
    path('hubungi-kami', views.KontakView.as_view(), name='kontak'),
    path('produk-kami', views.produk, name='produk'),
    path('pemesanan-kami', views.pemesanan, name='pemesanan'),
    path('checkout', views.checkout, name='checkout'),
    path('<slug:slug>', views.kategori, name='kategori')
    
]