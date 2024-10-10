from django import forms

from task_manager.transitions.models import Transition


class TransitionForm(forms.ModelForm):

    class Meta:
        model = Transition
        fields = [
            'name', 'volume', 'thickness', 'project_sheet', 'project'
        ]
        labels = {
            'name': 'Наименование',
            'volume': 'Объем',
            'thickness': 'Толщина',
            'project_sheet': 'Лист проекта',
            'project': 'Проект'
        }
