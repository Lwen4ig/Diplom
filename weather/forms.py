from .models import City
from django.forms import ModelForm, TextInput

class City_form(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-search', 'name': 'city', 'placeholder': 'Enter City'})}
