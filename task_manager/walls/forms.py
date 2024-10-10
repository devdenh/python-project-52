from django import forms

from task_manager.walls.models import Wall


class WallForm(forms.ModelForm):

    class Meta:
        model = Wall
        fields = [
            'name', 'volume', 'project_sheet', 'project'
        ]
        labels = {
            'name': 'Наименование стены',
            'volume': 'Объем',
            'project_sheet': 'Лист проекта',
            'project': 'Проект'
        }
