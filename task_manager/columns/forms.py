from django import forms
from django.forms import inlineformset_factory

from task_manager.columns.models import Column, ColumnArmature
from task_manager.forms import BaseArmatureForm
from task_manager.projects.models import Project


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
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


class ColumnArmatureForm(BaseArmatureForm):
    class Meta(BaseArmatureForm.Meta):
        model = ColumnArmature



ColumnArmatureFormSet = inlineformset_factory(
    Column,
    ColumnArmature,
    form=ColumnArmatureForm,
    extra=1,  # Количество пустых форм
    can_delete=True,
    can_delete_extra=True
)
