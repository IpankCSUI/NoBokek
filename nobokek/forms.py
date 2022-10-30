from django import forms

class Stat(forms.Form):
    harga_barang = forms.CharField(label='Title')
    date = forms.DateField()

class ContactForm(forms.Form):
    nama = forms.CharField(label="Nama", max_length=150)
    email = forms.EmailField(label="Email", widget=forms.Textarea)
    masalah = forms.CharField(label="Masalah", max_length=1000)