from django.urls import path
from . import views  # Pastikan views diimpor dengan benar

urlpatterns = [
    path('', views.index, name='index'),
    path('kain_terjual/', views.kain_terjual, name='kain_terjual'),
    path('toko_terkunjung/', views.toko_terkunjung, name='toko_terkunjung'),
    path('tanggal_terbanyak/', views.tanggal_terbanyak, name='tanggal_terbanyak'),
    path('pekerjaan_terbanyak/', views.pekerjaan_terbanyak, name='pekerjaan_terbanyak'),
    path('jenis_kelamin_terbanyak/', views.jenis_kelamin_terbanyak, name='jenis_kelamin_terbanyak'),
]

from django.shortcuts import render

def index(request):
    return render(request, 'laporan/index.html')