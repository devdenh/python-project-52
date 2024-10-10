from django import forms

from task_manager.sections.models import Section


class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['name', 'axes_location', 'bottom_floor_mark', 'absolute_zero_mark']
        labels = {
            'name': 'Наименование секции',
            'axes_location': 'Оси расположения',
            'bottom_floor_mark': 'Относительная отметка нуля',
            'absolute_zero_mark': 'Абсолютная отметка'
        }
