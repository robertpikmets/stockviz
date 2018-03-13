from django import forms
from compare.models import Ticker

class NewTicker(forms.ModelForm):
    class Meta():
        model = Ticker
        fields =  '__all__'
