from django.contrib import admin
from django.urls import path, include
from pembelian import views  # Impor views dari aplikasi pemesanan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),  # Root URL langsung menuju index dari aplikasi pemesanan
    path('laporan/', include('pembelian.urls')),  # Semua laporan tetap melalui aplikasi pemesanan
]