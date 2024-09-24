from django import forms

from task_manager.concrete.models import Concrete


class ConcreteForm(forms.ModelForm):

    class Meta:
        model = Concrete
        fields = ['klas', 'marka', 'strength_mpa']
        labels = {
            'klas': 'Класс',
            'marka': 'Марка',
            'strength_mpa': 'Прочность бетона'
        }
