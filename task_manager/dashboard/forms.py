import django_filters
from django import forms
from django.utils.translation import gettext as _

from task_manager.columns.models import Column
from task_manager.concrete.models import Concrete
from task_manager.dashboard.models import Dashboard
from task_manager.projects.models import Project
from task_manager.sections.models import Section
from task_manager.slabs.models import Slab
from task_manager.walls.models import Wall


class DashboardForm(forms.ModelForm):

    projects = forms.ModelMultipleChoiceField(
        label=_("Projects"),
        queryset=Project.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    sections = forms.ModelMultipleChoiceField(
        label=_("Sections"),
        queryset=Section.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    concrete = forms.ModelMultipleChoiceField(
        label=_("Concrete"),
        queryset=Concrete.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    columns = forms.ModelMultipleChoiceField(
        label=_("Columns"),
        queryset=Column.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    walls = forms.ModelMultipleChoiceField(
        label=_("Walls"),
        queryset=Wall.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    slabs = forms.ModelMultipleChoiceField(
        label=_("Slabs"),
        queryset=Slab.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )


class DashboardFilterForm(django_filters.FilterSet):

    project = django_filters.ModelChoiceFilter(
        field_name='project',
        queryset=Project.objects.all(),
        label=_("Project")
    )

    section = django_filters.ModelChoiceFilter(
        field_name='section',
        queryset=Section.objects.all(),
        label=_("Section")
    )

    concrete = django_filters.ModelChoiceFilter(
        field_name='concrete',
        queryset=Concrete.objects.all(),
        label=_("Concrete")
    )

    column = django_filters.ModelChoiceFilter(
        field_name='column',
        queryset=Column.objects.all(),
        label=_("Column")
    )

    wall = django_filters.ModelChoiceFilter(
        field_name='wall',
        queryset=Wall.objects.all(),
        label=_("Wall")
    )

    slab = django_filters.ModelChoiceFilter(
        field_name='slab',
        queryset=Slab.objects.all(),
        label=_("Slab")
    )

    class Meta:
        model = Dashboard  # или любая другая основная модель, которую используешь для связей
        fields = ["project", "section", "concrete", "column", "wall", "slab"]
