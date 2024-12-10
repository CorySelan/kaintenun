from django.contrib import admin
from .models import Pembeli, NomorHp, KainTenun, Toko, Pembelian, DetailPembelian, Kepemilikan

class NomorHpAdmin(admin.ModelAdmin):
    list_display = ('idNomorHp', 'idPembeli', 'nomorHp')  # Menampilkan kolom ID, Pembeli, dan Nomor HP
    search_fields = ('idPembeli__namaDepan', 'nomorHp')  # Memungkinkan pencarian berdasarkan Nama Depan Pembeli atau Nomor HP
    list_filter = ('idPembeli__jenisKelamin',)  # Memungkinkan filter berdasarkan Jenis Kelamin Pembeli

class KainTenunAdmin(admin.ModelAdmin):
    list_display = ('idKainTenun', 'namaKainTenun', 'harga', 'deskripsiKainTenun')  # Menampilkan kolom ID, Nama, Harga, dan Deskripsi Kain Tenun
    search_fields = ('namaKainTenun',)  # Memungkinkan pencarian berdasarkan Nama Kain Tenun
    list_filter = ('harga',)  # Memungkinkan filter berdasarkan Harga

class TokoAdmin(admin.ModelAdmin):
    list_display = ('idToko', 'namaToko', 'alamat')  # Menampilkan kolom ID, Nama, dan Alamat Toko
    search_fields = ('namaToko',)  # Memungkinkan pencarian berdasarkan Nama Toko
    list_filter = ('alamat',)  # Memungkinkan filter berdasarkan Alamat Toko

class PembelianAdmin(admin.ModelAdmin):
    list_display = ('idPembelian', 'idPembeli', 'idToko', 'tanggalPembelian')  # Menampilkan kolom ID Pembelian, Pembeli, Toko, dan Tanggal Pembelian
    search_fields = ('idPembeli__namaDepan', 'idToko__namaToko')  # Memungkinkan pencarian berdasarkan Nama Pembeli dan Nama Toko
    list_filter = ('tanggalPembelian',)  # Memungkinkan filter berdasarkan Tanggal Pembelian

class DetailPembelianAdmin(admin.ModelAdmin):
    readonly_fields = ('idDetailPembelian',)  # Jadikan ID Detail Pembelian read-only
    list_display = ('idDetailPembelian', 'idPembelian', 'idKainTenun')  # Menampilkan kolom ID Detail Pembelian, ID Pembelian, dan Kain Tenun
    search_fields = ('idPembelian__idPembelian', 'idKainTenun__namaKainTenun')  # Memungkinkan pencarian berdasarkan ID Pembelian dan Nama Kain Tenun

class KepemilikanAdmin(admin.ModelAdmin):
    list_display = ('idKepemilikan', 'idKainTenun', 'idToko', 'stok')  # Menampilkan kolom ID Kepemilikan, Kain Tenun, Toko, dan Stok
    search_fields = ('idKainTenun__namaKainTenun', 'idToko__namaToko')  # Memungkinkan pencarian berdasarkan Nama Kain Tenun dan Nama Toko
    list_filter = ('stok',)  # Memungkinkan filter berdasarkan Stok

# Register the models with the admin interface
admin.site.register(Pembeli)
admin.site.register(NomorHp, NomorHpAdmin)
admin.site.register(KainTenun, KainTenunAdmin)
admin.site.register(Toko, TokoAdmin)
admin.site.register(Pembelian, PembelianAdmin)
admin.site.register(DetailPembelian, DetailPembelianAdmin)
admin.site.register(Kepemilikan, KepemilikanAdmin)
