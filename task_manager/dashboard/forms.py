import django_filters
from django import forms
from django.db.models import Sum
from django.utils.translation import gettext as _

from task_manager.columns.models import Column
from task_manager.concrete.models import Concrete
from task_manager.dashboard.models import Dashboard
from task_manager.floors.models import Floor
from task_manager.links.cfs.models import CFS
from task_manager.links.sfs.models import SFS
from task_manager.links.tfs.models import TFS
from task_manager.links.wfs.models import WFS
from task_manager.projects.models import Project
from task_manager.sections.models import Section
from task_manager.slabs.models import Slab
from task_manager.transitions.models import Transition
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

    concrete = django_filters.ModelMultipleChoiceFilter(
        field_name='concrete',
        queryset=Concrete.objects.all(),
        label="Бетон",
    )

    section = django_filters.ModelMultipleChoiceFilter(
        field_name='section',
        queryset=Section.objects.all(),
        label=_("Секция")
    )

    column = django_filters.ModelMultipleChoiceFilter(
        field_name='column',
        queryset=Column.objects.all(),
        label=_("Колонна"),
    )

    wall = django_filters.ModelMultipleChoiceFilter(
        field_name='wall',
        queryset=Wall.objects.all(),
        label=_("Стена")
    )

    slab = django_filters.ModelMultipleChoiceFilter(
        field_name='slab',
        queryset=Slab.objects.all(),
        label=_("Перекрытие")
    )

    floor = django_filters.ModelMultipleChoiceFilter(
        field_name='floor',
        queryset=Floor.objects.all(),
        label=_("Этаж")
    )

    transition = django_filters.ModelMultipleChoiceFilter(
        field_name='transition',
        queryset=Transition.objects.all(),
        label=_("Площадка")
    )


    @property
    def qs(self):
        parent_qs = super().qs

        # Получаем фильтруемые значения
        section = self.data.get('section')
        concrete = self.data.get('concrete')
        column = self.data.get('column')
        walls = self.data.get('wall')
        slab = self.data.get('slab')
        floor = self.data.get('floor')
        transition = self.data.get('transition')

        # Начальная выборка всех записей
        cfs_qs = CFS.objects.select_related('column').all()
        sfs_qs = SFS.objects.select_related('slab').all()
        tfs_qs = TFS.objects.select_related('transition').all()
        wfs_qs = WFS.objects.select_related('wall').all()


        # Фильтрация по конкретному бетону
        if concrete:
            cfs_qs = cfs_qs.filter(concrete__in=self.data.getlist('concrete'))
            sfs_qs = sfs_qs.filter(concrete__in=self.data.getlist('concrete'))
            tfs_qs = tfs_qs.filter(concrete__in=self.data.getlist('concrete'))
            wfs_qs = wfs_qs.filter(concrete__in=self.data.getlist('concrete'))


        # Фильтрация по секции
        if section:
            sections = self.data.getlist('section')
            cfs_qs = cfs_qs.filter(section__in=sections)
            sfs_qs = sfs_qs.filter(section__in=sections)
            tfs_qs = tfs_qs.filter(section__in=sections)
            wfs_qs = wfs_qs.filter(section__in=sections)


        # Фильтрация по этажу
        if floor:
            floors = self.data.getlist('floor')
            cfs_qs = cfs_qs.filter(floor__in=floors)
            sfs_qs = sfs_qs.filter(floor__in=floors)
            tfs_qs = tfs_qs.filter(floor__in=floors)
            wfs_qs = wfs_qs.filter(floor__in=floors)


        querysets = []

        # Фильтрация по стенам, если выбран множественный фильтр
        if walls:
            querysets.append(wfs_qs.filter(wall__in=self.data.getlist('wall')))
        if slab:
            querysets.append(sfs_qs.filter(slab__in=self.data.getlist('slab')))
        if transition:
            querysets.append(tfs_qs.filter(transition__in=self.data.getlist('transition')))
        if column:
            querysets.append(cfs_qs.filter(column__in=self.data.getlist('column')))

        # Если ничего конкретного не выбрано, показываем все
        if not any([slab, transition, column, walls]):
            querysets.extend([sfs_qs, tfs_qs, wfs_qs, cfs_qs])

        # Выбранные фильтры
        self.active_filters = {}
        if self.data:
            self.active_filters = {
                field.label: field.queryset.filter(id__in=self.data.getlist(field_name))
                for field_name, field in self.form.fields.items()
            }


        # Объединяем все QuerySet'ы в один результат
        result_list = sum(map(list, querysets), [])


        return result_list

    def calculate_total_volume(self):
        filtered_cfs_qs = CFS.objects.filter(id__in=[obj.id for obj in self.qs if isinstance(obj, CFS)])
        filtered_sfs_qs = SFS.objects.filter(id__in=[obj.id for obj in self.qs if isinstance(obj, SFS)])
        filtered_tfs_qs = TFS.objects.filter(id__in=[obj.id for obj in self.qs if isinstance(obj, TFS)])
        filtered_wfs_qs = WFS.objects.filter(id__in=[obj.id for obj in self.qs if isinstance(obj, WFS)])

        cfs_volume = filtered_cfs_qs.aggregate(Sum('column__volume'))['column__volume__sum'] or 0
        sfs_volume = filtered_sfs_qs.aggregate(Sum('slab__volume'))['slab__volume__sum'] or 0
        tfs_volume = filtered_tfs_qs.aggregate(Sum('transition__volume'))['transition__volume__sum'] or 0
        wfs_volume = filtered_wfs_qs.aggregate(Sum('wall__volume'))['wall__volume__sum'] or 0

        total_volume = cfs_volume + sfs_volume + tfs_volume + wfs_volume
        return round(total_volume, 2)
