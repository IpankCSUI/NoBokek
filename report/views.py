from django.shortcuts import render
from report.models import BarangWishlist



def show_report(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Kak Cinoy'
    }
    return render(request, "report.html")


