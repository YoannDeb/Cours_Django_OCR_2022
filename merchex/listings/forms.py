from django import forms

from .models import Band

class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'