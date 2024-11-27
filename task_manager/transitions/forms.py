from django import forms
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render

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
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'volume': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'thickness': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'project_sheet': forms.TextInput(attrs={'class': 'form-control'}),
        #     'project': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class TransitionArmatureForm(forms.ModelForm):
    class Meta:
        model = TransitionArmature
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
        # widgets = {
        #     'diameter': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'klas': forms.TextInput(attrs={'class': 'form-control'}),
        #     'bar_length': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'bar_count': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'bar_type': forms.TextInput(attrs={'class': 'form-control'}),
        #     'manufacture_place': forms.TextInput(attrs={'class': 'form-control'}),
        # }


TransitionArmatureFormSet = inlineformset_factory(
    Transition,
    TransitionArmature,
    form=TransitionArmatureForm,
    extra=1,  # Количество пустых форм,
    can_delete=True,
    can_delete_extra=True
)
