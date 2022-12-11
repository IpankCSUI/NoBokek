from dataclasses import field
from django import forms
from .models import PendapatForum

class AddPendapatForum(forms.ModelForm):
    class Meta:
        model = PendapatForum
        fields = '__all__'
        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'jurusan':forms.TextInput(attrs={'class':'form-control'}),
            'angkatan':forms.TextInput(attrs={'class':'form-control'}),
            'pendapat':forms.Textarea(attrs={'class':'form-control'}),
        }