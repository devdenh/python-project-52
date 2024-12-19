from django import forms
from django.forms import inlineformset_factory

from task_manager.projects.models import Project
from task_manager.walls.models import Wall
from task_manager.walls.models import WallArmature


class WallForm(forms.ModelForm):
    class Meta:
        model = Wall
        fields = ['name', 'volume', 'project_sheet', 'project']
        labels = {
            'name': 'Наименование',
            'volume': 'Объем',
            'project_sheet': 'Лист проекта',
            'project': 'Проект'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'class': 'form-control'}),
            'project_sheet': forms.TextInput(attrs={'class': 'form-control'}),
        }

    project = forms.ModelChoiceField(
        label=Meta.labels['project'],
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Выберите проект"
    )


class WallArmatureForm(forms.ModelForm):
    class Meta:
        model = WallArmature
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

WallArmatureFormSet = inlineformset_factory(
    Wall,
    WallArmature,
    form=WallArmatureForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True
)
