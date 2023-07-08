from django import forms
from .models import Paginas, UserNueva

class PagsForm (forms.ModelForm):
    class Meta:
        model = Paginas
        fields = '__all__'

class UserForm (forms.ModelForm):
    class Meta:
        model = UserNueva
        fields = '__all__'