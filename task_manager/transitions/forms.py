from django import forms
from django.forms import inlineformset_factory

from task_manager.forms import BaseArmatureForm
from task_manager.projects.models import Project
from task_manager.transitions.models import Transition, TransitionArmature


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


class TransitionArmatureForm(BaseArmatureForm):
    class Meta(BaseArmatureForm.Meta):
        model = TransitionArmature


TransitionArmatureFormSet = inlineformset_factory(
    Transition,
    TransitionArmature,
    form=TransitionArmatureForm,
    extra=1,  # Количество пустых форм,
    can_delete=True,
    can_delete_extra=True
)
