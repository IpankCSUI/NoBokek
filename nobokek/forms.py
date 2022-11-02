from django import forms
from nobokek.models import ContactUs

class ContactForm(forms.ModelForm):
    nama = forms.TextInput()
    alamat = forms.TextInput()
    masalah = forms.Textarea()

    class Meta:
        model = ContactUs
        fields = [
            "nama",
            "alamat",
            "masalah"
        ]
        widgets = {
           'nama' : forms.TextInput(attrs={
            'id':'nama'
           }),
           'alamat' : forms.TextInput(attrs={
            'id':'alamat'
           }),
           'masalah' : forms.Textarea(attrs={
            'id':'masalah'
           }),
        }