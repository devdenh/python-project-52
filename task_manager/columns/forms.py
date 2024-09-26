from django import forms

from task_manager.columns.models import Column


class ColumnForm(forms.ModelForm):

    class Meta:
        model = Column
        fields = [
            'name', 'length', 'width',
        ]
        labels = {
            'name': 'Наименование колонны',
            'length': 'Длина в сечении',
            'width': 'Ширина в сечении'
        }
