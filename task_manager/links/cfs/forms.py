from django import forms
from .models import CFS


class CFSForm(forms.ModelForm):
    class Meta:
        model = CFS
        fields = ['column', 'floor', 'section', 'concrete', 'axes']
        labels = {
            'column': 'Колонна',
            'floor': 'Этаж',
            'section': 'Секция',
            'concrete': 'Бетон',
            'axes': 'Оси'
        }
