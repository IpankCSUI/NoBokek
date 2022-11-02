from django import forms
from django import forms
from add.models import Money
from django.core.exceptions import NON_FIELD_ERRORS

# class AddIncomeOutcome(forms.Form):
#     income = forms.FloatField('id':'income')
#     outcome = forms.FloatField('id':'outcome')
#     desc_in = forms.CharField(max_length=255, 'id':'desc_in')
#     desc_out = forms.CharField(max_length=255, 'id':'desc_out')

class AddIncomeOutcome(forms.ModelForm):
    class Meta:
        model = Money
        fields = [
            "income",
            "outcome",
            "desc_in",
            "desc_out"
        ]
        widgets = {
           'income' : forms.NumberInput(attrs={
            'id':'income'
           }),
           'outcome' : forms.NumberInput(attrs={
            'id':'outcome'
           }),
           'desc_in' : forms.TextInput(attrs={
            'id':'desc_in'
           }),
           'desc_out' : forms.TextInput(attrs={
            'id':'desc_out'
           }),
        }
   