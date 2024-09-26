from django import forms

from task_manager.walls.models import Wall


class WallForm(forms.ModelForm):

    class Meta:
        model = Wall
        fields = [
            'name', 'volume', 'thickness', 'section_floor'
        ]
        labels = {
            'name': 'Наименование стены',
            'volume': 'Объем',
            'thickness': 'Толщина',
            'section_floor': 'Связь с этажом секции'
        }
