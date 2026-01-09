from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('kategori/', views.kategori_list),
    path('kategori/tambah/', views.kategori_tambah),
    path('kategori/hapus/<int:id>/', views.kategori_hapus),

    path('produk/', views.produk_list),
    path('produk/tambah/', views.produk_tambah),

    path('transaksi/', views.transaksi),
    path('transaksi/riwayat/', views.transaksi_riwayat),
    path('transaksi/<int:id>/', views.transaksi_detail),
]
