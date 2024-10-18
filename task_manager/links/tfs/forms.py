from django import forms
from .models import TFS


class TFSForm(forms.ModelForm):
    class Meta:
        model = TFS
        fields = ['transition', 'floor', 'section', 'concrete', 'axes']
        labels = {
            'transition': 'Лестничная площадка',
            'floor': 'Этаж',
            'section': 'Секция',
            'concrete': 'Бетон',
            'axes': 'Оси'
        }
