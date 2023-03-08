from django import forms
from .models import MyModel


class ProductForm(forms.ModelForm):
    excel_file = forms.FileField()

    class Meta:
        model = MyModel
        fields = '__all__'
