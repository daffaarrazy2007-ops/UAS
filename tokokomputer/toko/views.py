from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction as db_transaction
from .models import Kategori, Produk, Transaksi, DetailTransaksi


# ===== HOME =====
def home(request):
    return redirect('/produk/')


# =========================
# ===== KATEGORI =====
# =========================
def kategori_list(request):
    data = Kategori.objects.all()
    return render(request, 'kategori.html', {'data': data})


def kategori_tambah(request):
    if request.method == "POST":
        nama = request.POST.get('nama')
        if nama:
            Kategori.objects.create(nama=nama)
            return redirect('/kategori/')
    return render(request, 'kategori_tambah.html')


def kategori_hapus(request, id):
    kategori = get_object_or_404(Kategori, id=id)
    kategori.delete()
    return redirect('/kategori/')


# =========================
# ===== PRODUK =====
# =========================
def produk_list(request):
    produk = Produk.objects.select_related('kategori').all()
    return render(request, 'produk.html', {'produk': produk})


def produk_tambah(request):
    kategori = Kategori.objects.all()

    if request.method == "POST":
        nama = request.POST.get('nama')
        harga = request.POST.get('harga')
        stok = request.POST.get('stok')
        kategori_id = request.POST.get('kategori')

        if not kategori_id:
            return render(request, 'produk_tambah.html', {
                'kategori': kategori,
                'error': 'Kategori wajib dipilih'
            })

        Produk.objects.create(
            nama=nama,
            harga=harga,
            stok=stok,
            kategori_id=kategori_id
        )
        return redirect('/produk/')

    return render(request, 'produk_tambah.html', {'kategori': kategori})


def produk_hapus(request, id):
    produk = get_object_or_404(Produk, id=id)
    produk.delete()
    return redirect('/produk/')


# =========================
# ===== TRANSAKSI =====
# =========================
def transaksi(request):
    produk = Produk.objects.all()

    if request.method == "POST":
        transaksi = Transaksi.objects.create(total=0)
        total = 0

        with db_transaction.atomic():
            for p in produk:
                qty = int(request.POST.get(str(p.id), 0))
                if qty > 0:
                    if p.stok < qty:
                        return render(request, 'transaksi.html', {
                            'produk': produk,
                            'error': f'Stok {p.nama} tidak mencukupi'
                        })

                    subtotal = qty * p.harga

                    DetailTransaksi.objects.create(
                        transaksi=transaksi,
                        produk=p,
                        jumlah=qty,
                        subtotal=subtotal
                    )

                    p.stok -= qty
                    p.save()

                    total += subtotal

        transaksi.total = total
        transaksi.save()

        return redirect(f'/transaksi/{transaksi.id}/')

    return render(request, 'transaksi.html', {'produk': produk})


def transaksi_detail(request, id):
    transaksi = get_object_or_404(Transaksi, id=id)
    detail = DetailTransaksi.objects.filter(transaksi=transaksi)

    return render(request, 'transaksi_detail.html', {
        'transaksi': transaksi,
        'detail': detail
    })

def transaksi_riwayat(request):
    transaksi = Transaksi.objects.all().order_by('-tanggal')
    return render(request, 'transaksi_riwayat.html', {
        'transaksi': transaksi
    })
