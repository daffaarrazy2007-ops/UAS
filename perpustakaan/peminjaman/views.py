from django.shortcuts import render, redirect, get_object_or_404
from .models import Peminjaman
from .forms import PeminjamanForm

# READ (Menampilkan semua data)
def index(request):
    data = Peminjaman.objects.all()
    return render(request, 'peminjaman/index.html', {'data': data})

# CREATE (Menambah data baru)
def create(request):
    form = PeminjamanForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'peminjaman/form.html', {'form': form, 'title': 'Tambah Peminjaman'})

# UPDATE (Mengubah data)
def update(request, id):
    obj = get_object_or_404(Peminjaman, id=id)
    form = PeminjamanForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'peminjaman/form.html', {'form': form, 'title': 'Edit Peminjaman'})

# DELETE (Menghapus data)
def delete(request, id):
    obj = get_object_or_404(Peminjaman, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('index')
    return render(request, 'peminjaman/delete_confirm.html', {'obj': obj})