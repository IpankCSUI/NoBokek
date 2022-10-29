from django import forms

class Stat(forms.Form):
    harga_barang = forms.CharField(label='Title')
    date = forms.DateField()