from django.db import models

class Peminjaman(models.Model):
    # Pilihan untuk status
    STATUS_CHOICES = [
        ('Dipinjam', 'Dipinjam'),
        ('Dikembalikan', 'Dikembalikan'),
    ]

    nama_peminjam = models.CharField(max_length=100)
    judul_buku = models.CharField(max_length=150)
    pengarang = models.CharField(max_length=100)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Dipinjam'  # Menambahkan default agar saat input baru otomatis 'Dipinjam'
    )

    def __str__(self):
        # Mengembalikan nama peminjam dan judul buku agar lebih informatif di Admin
        return f"{self.nama_peminjam} - {self.judul_buku}"

    class Meta:
        verbose_name_plural = "Data Peminjaman"