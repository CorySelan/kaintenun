from django.db import models
from django.utils.translation import gettext_lazy as _

# Model Pembeli
class Pembeli(models.Model):
    GENDER_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]

    idPembeli = models.CharField(max_length=15, verbose_name='ID Pembeli', primary_key=True)
    namaDepan = models.CharField(max_length=35, verbose_name='Nama Depan')
    namaBelakang = models.CharField(max_length=35, verbose_name='Nama Belakang')
    jenisKelamin = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Jenis Kelamin')
    tanggalLahir = models.DateField(verbose_name='Tanggal Lahir')
    pekerjaan = models.CharField(max_length=35, verbose_name='Pekerjaan')
    alamat = models.TextField(verbose_name='Alamat')

    class Meta:
        verbose_name_plural = 'Pembeli'

    def __str__(self):
        return f"{self.namaDepan} {self.namaBelakang}"

# Model Nomor HP
class NomorHp(models.Model):
    idNomorHp = models.AutoField(primary_key=True)
    idPembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE)
    nomorHp = models.CharField(max_length=15, null=False, verbose_name='Nomor HP')

    class Meta:
        verbose_name_plural = 'Nomor HP'

    def __str__(self):
        return f"{self.nomorHp} - {self.idPembeli}"

# Model Kain Tenun
class KainTenun(models.Model):
    idKainTenun = models.CharField(max_length=15, verbose_name='ID Kain Tenun', primary_key=True)
    namaKainTenun = models.CharField(max_length=100, null=False, default="", verbose_name='Nama Kain Tenun')
    harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Harga')
    deskripsiKainTenun = models.TextField(verbose_name='Deskripsi Kain Tenun')  # Diubah menjadi TextField

    class Meta:
        verbose_name_plural = 'Kain Tenun'

    def __str__(self):
        return self.namaKainTenun

# Model Toko
class Toko(models.Model):
    idToko = models.CharField(max_length=15, verbose_name='ID Toko', primary_key=True)
    namaToko = models.CharField(max_length=50, null=False, default="", verbose_name='Nama Toko')
    alamat = models.TextField(null=True, blank=True, verbose_name='Alamat')

    class Meta:
        verbose_name_plural = 'Toko'

    def __str__(self):
        return f"{self.namaToko} (ID: {self.idToko})"

# Model Pembelian
class Pembelian(models.Model):
    idPembelian = models.AutoField(primary_key=True)
    idPembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE, verbose_name='ID Pembeli')
    idToko = models.ForeignKey(Toko, on_delete=models.CASCADE, verbose_name='ID Toko')
    tanggalPembelian = models.DateField(verbose_name='Tanggal Pembelian')

    class Meta:
        verbose_name_plural = 'Pembelian'

    def __str__(self):
        return f"Pembelian {self.idPembelian} oleh {self.idPembeli}"

# Model Detail Pembelian
class DetailPembelian(models.Model):
    idDetailPembelian = models.AutoField(primary_key=True)
    idPembelian = models.ForeignKey(Pembelian, on_delete=models.CASCADE, related_name='detail_pembelian', verbose_name='ID Pembelian')
    idKainTenun = models.ForeignKey(KainTenun, on_delete=models.CASCADE, verbose_name='ID Kain Tenun')

    class Meta:
        verbose_name_plural = 'Detail Pembelian'

    def __str__(self):
        return f"Detail Pembelian {self.idDetailPembelian} - Kain {self.idKainTenun}"

# Model Kepemilikan
class Kepemilikan(models.Model):
    idKepemilikan = models.AutoField(primary_key=True)
    idKainTenun = models.ForeignKey(KainTenun, on_delete=models.CASCADE, verbose_name='ID Kain Tenun')
    idToko = models.ForeignKey(Toko, on_delete=models.CASCADE, verbose_name='ID Toko')
    stok = models.IntegerField(null=False, default=0, verbose_name='Stok')

    class Meta:
        verbose_name_plural = 'Kepemilikan'

    def __str__(self):
        return f"Kepemilikan {self.idKepemilikan} - Stok: {self.stok}"
