from django.shortcuts import render
from django.db.models import Count
from pembelian.models import Pembeli, DetailPembelian, Pembelian, Toko, KainTenun

def index(request):
    return render(request, 'laporan/index.html')  # Menampilkan laporan/index.html

# View untuk laporan kain terjual
def kain_terjual(request):
    # Query untuk menghitung jumlah kain terjual
    kain_terjual_data = (
        DetailPembelian.objects
        .values('idKainTenun', 'idKainTenun__namaKainTenun')  # Ambil id dan nama kain
        .annotate(jumlah_terjual=Count('idKainTenun'))  # Hitung jumlah terjual
        .order_by('-jumlah_terjual')  # Urutkan berdasarkan jumlah terjual
    )

    # Data untuk template
    kain_terjual = [
        {
            'namaKainTenun': item['idKainTenun__namaKainTenun'],  # Nama kain
            'jumlah_terjual': item['jumlah_terjual'],  # Jumlah terjual
        }
        for item in kain_terjual_data
    ]

    return render(request, 'laporan/kain_terjual.html', {'kain_terjual': kain_terjual})
# View untuk laporan toko yang paling sering dikunjungi
def toko_terkunjung(request):
    # Menghitung jumlah kunjungan ke setiap toko
    toko_terkunjung_data = (Pembelian.objects
                            .values('idToko')  # Mengelompokkan berdasarkan idToko
                            .annotate(jumlah_kunjungan=Count('idToko'))  # Menghitung jumlah kunjungan
                            .order_by('-jumlah_kunjungan'))  # Mengurutkan berdasarkan jumlah kunjungan terbanyak

    # Mengambil data toko dan jumlah kunjungan
    toko_terkunjung = []
    for item in toko_terkunjung_data:
        toko = Toko.objects.get(idToko=item['idToko'])
        toko_terkunjung.append({
            'namaToko': toko.namaToko,
            'jumlah_kunjungan': item['jumlah_kunjungan'],
        })

    return render(request, 'laporan/toko_terkunjung.html', {'toko_terkunjung': toko_terkunjung})


# View untuk laporan tanggal dengan pembelian terbanyak
def tanggal_terbanyak(request):
    # Menghitung jumlah pembelian berdasarkan tanggal
    tanggal_terbanyak_data = (Pembelian.objects
                              .values('tanggalPembelian')  # Mengelompokkan berdasarkan tanggal pembelian
                              .annotate(jumlah_pembelian=Count('tanggalPembelian'))  # Menghitung jumlah pembelian
                              .order_by('-jumlah_pembelian'))  # Mengurutkan berdasarkan jumlah pembelian terbanyak

    # Mengambil data tanggal dan jumlah pembelian
    tanggal_terbanyak = []
    for item in tanggal_terbanyak_data:
        tanggal_terbanyak.append({
            'tanggalPembelian': item['tanggalPembelian'],
            'jumlah_pembelian': item['jumlah_pembelian'],
        })

    return render(request, 'laporan/tanggal_terbanyak.html', {'tanggal_terbanyak': tanggal_terbanyak})


# View untuk laporan pekerjaan pembeli terbanyak
def pekerjaan_terbanyak(request):
    # Menghitung jumlah pembelian berdasarkan pekerjaan
    pekerjaan_terbanyak_data = (Pembeli.objects
                                .values('pekerjaan')  # Mengelompokkan berdasarkan pekerjaan pembeli
                                .annotate(jumlah_pembelian=Count('pembelian'))  # Menghitung jumlah pembelian
                                .order_by('-jumlah_pembelian'))  # Mengurutkan berdasarkan jumlah pembelian terbanyak

    # Mengambil data pekerjaan dan jumlah pembelian
    pekerjaan_terbanyak = []
    for item in pekerjaan_terbanyak_data:
        pekerjaan_terbanyak.append({
            'pekerjaan': item['pekerjaan'],
            'jumlah_pembelian': item['jumlah_pembelian'],
        })

    return render(request, 'laporan/pekerjaan_terbanyak.html', {'pekerjaan_terbanyak': pekerjaan_terbanyak})


# View untuk laporan jenis kelamin pembeli terbanyak
def jenis_kelamin_terbanyak(request):
    # Menghitung jumlah pembelian berdasarkan jenis kelamin
    jenis_kelamin_terbanyak_data = (Pembeli.objects
                                    .values('jenisKelamin')  # Mengelompokkan berdasarkan jenis kelamin
                                    .annotate(jumlah_pembelian=Count('pembelian'))  # Menghitung jumlah pembelian
                                    .order_by('-jumlah_pembelian'))  # Mengurutkan berdasarkan jumlah pembelian terbanyak

    # Mengambil data jenis kelamin dan jumlah pembelian
    jenis_kelamin_terbanyak = []
    for item in jenis_kelamin_terbanyak_data:
        jenis_kelamin = 'Pria' if item['jenisKelamin'] == 'P' else 'Wanita'
        jenis_kelamin_terbanyak.append({
            'jenis_kelamin': jenis_kelamin,
            'jumlah_pembelian': item['jumlah_pembelian'],
        })

    return render(request, 'laporan/jenis_kelamin_terbanyak.html', {'jenis_kelamin_terbanyak': jenis_kelamin_terbanyak})
