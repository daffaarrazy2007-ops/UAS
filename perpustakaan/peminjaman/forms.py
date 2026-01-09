from django import forms
from .models import Peminjaman

class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = [
            'nama_peminjam',
            'judul_buku',
            'pengarang',
            'tanggal_pinjam',
            'tanggal_kembali',
            'status'
        ]
        # Menambahkan widget agar input tanggal muncul kalender
        widgets = {
            'tanggal_pinjam': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_kembali': forms.DateInput(attrs={'type': 'date'}),
        }