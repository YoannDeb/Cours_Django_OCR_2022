from django import forms

from .models import Band, Listing

class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ('sold',)

