from django import forms
from .models import WFS


class WFSForm(forms.ModelForm):
    class Meta:
        model = WFS
        fields = ['wall', 'floor', 'section', 'concrete', 'axes']
        labels = {
            'wall': 'Стена',
            'floor': 'Этаж',
            'section': 'Секция',
            'concrete': 'Бетон',
            'axes': 'Оси'
        }
