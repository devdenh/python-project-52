from django import forms

from task_manager.slabs.models import Slab


class SlabForm(forms.ModelForm):

    class Meta:
        model = Slab
        fields = [
            'name', 'volume', 'thickness', 'project_sheet', 'project'
        ]
        labels = {
            'name': 'Наименование перекрытия',
            'volume': 'Объем',
            'thickness': 'Толщина',
            'project_sheet': 'Лист проекта',
            'project': 'Проект'
        }
