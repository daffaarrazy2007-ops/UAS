from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Produk(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.IntegerField()
    stok = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama


class Transaksi(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)


class DetailTransaksi(models.Model):
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    subtotal = models.IntegerField()
