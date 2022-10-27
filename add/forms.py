from django import forms
from django import forms

class AddIncomeOutcome(forms.Form):
    income = forms.FloatField()
    outcome = forms.FloatField()
    desc_in = forms.CharField(max_length=255)
    desc_out = forms.CharField(max_length=255)