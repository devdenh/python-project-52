from django import forms
from .models import SFS


class SFSForm(forms.ModelForm):
    class Meta:
        model = SFS
        fields = ['slab', 'floor', 'section', 'concrete', 'axes']
        labels = {
            'slab': 'Перекрытие',
            'floor': 'Этаж',
            'section': 'Секция',
            'concrete': 'Бетон',
            'axes': 'Оси'
        }

