from django import forms # type: ignore
from .models import Person


class RideForm(forms.Form):
  search = forms.CharField(label='Search term', max_length=64, required=False)


class NewRideForm(forms.ModelForm):
  class Meta:
    model = Person
    exclude = []
