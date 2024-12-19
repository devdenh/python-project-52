from django import forms
from django.forms import inlineformset_factory

from task_manager.forms import BaseArmatureForm
from task_manager.projects.models import Project
from task_manager.slabs.models import Slab, SlabArmature


class SlabForm(forms.ModelForm):
    class Meta:
        model = Slab
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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'}),
            'thickness': forms.TextInput(attrs={'class': 'form-control'}),
            'project_sheet': forms.TextInput(attrs={'class': 'form-control'}),
        }

    project = forms.ModelChoiceField(
        label=Meta.labels['project'],
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Выберите проект"
    )

class SlabArmatureForm(BaseArmatureForm):
    class Meta:
        model = SlabArmature
        fields = [
            'diameter', 'klas', 'bar_length', 'bar_count',
            'bar_type', 'manufacture_place'
        ]
        labels = {
            'diameter': 'Диаметр',
            'klas': 'Класс',
            'bar_length': 'Длина стержней',
            'bar_count': 'Количество стержней',
            'bar_type': 'Вид стержня',
            'manufacture_place': 'Место изготовления'
        }


SlabArmatureFormSet = inlineformset_factory(
    Slab,
    SlabArmature,
    form=SlabArmatureForm,
    extra=1,  # Количество пустых форм,
    can_delete=True,
    can_delete_extra=True
)
