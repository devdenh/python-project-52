from django import forms

from task_manager.columns.models import Column


class ColumnForm(forms.ModelForm):

    class Meta:
        model = Column
        fields = [
            'name', 'volume', 'project_sheet', 'project'
        ]
        labels = {
            'name': 'Наименование колонны',
            'volume': 'Объем',
            'project_sheet': 'Лист проекта',
            'project': 'Проект'
        }
