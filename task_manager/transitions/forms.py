from django import forms

from task_manager.transitions.models import Transition


class TransitionForm(forms.ModelForm):

    class Meta:
        model = Transition
        fields = [
            'name', 'volume', 'thickness'
        ]
        labels = {
            'name': 'Наименование',
            'volume': 'Объем',
            'thickness': 'Толщина',
        }
