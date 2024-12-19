import django_filters
from django.db.models import Sum

from task_manager.armatures.models import Armature
from task_manager.armaturesklas.models import ArmatureKlas
from task_manager.columns.models import Column
from task_manager.concrete.models import Concrete
from task_manager.floors.models import Floor
from task_manager.links.cfs.models import CFS
from task_manager.links.sfs.models import SFS
from task_manager.links.tfs.models import TFS
from task_manager.links.wfs.models import WFS
from task_manager.models import BaseArmature
from task_manager.sections.models import Section
from task_manager.slabs.models import Slab
from task_manager.transitions.models import Transition, TransitionArmature
from task_manager.walls.models import Wall


class DashboardFilterForm(django_filters.FilterSet):

    concrete = django_filters.ModelMultipleChoiceFilter(
        field_name='concrete',
        queryset=Concrete.objects.all(),
        label="Бетон",
    )

    section = django_filters.ModelMultipleChoiceFilter(
        field_name='section',
        queryset=Section.objects.all(),
        label="Секция"
    )

    column = django_filters.ModelMultipleChoiceFilter(
        field_name='column',
        queryset=Column.objects.all(),
        label="Колонна",
    )

    wall = django_filters.ModelMultipleChoiceFilter(
        field_name='wall',
        queryset=Wall.objects.all(),
        label="Стена"
    )

    slab = django_filters.ModelMultipleChoiceFilter(
        field_name='slab',
        queryset=Slab.objects.all(),
        label="Перекрытие"
    )

    floor = django_filters.ModelMultipleChoiceFilter(
        field_name='floor',
        queryset=Floor.objects.all(),
        label="Этаж"
    )

    transition = django_filters.ModelMultipleChoiceFilter(
        field_name='transition',
        queryset=Transition.objects.all(),
        label="Площадка"
    )

    armature_klas = django_filters.ModelMultipleChoiceFilter(
        field_name='armature_klas',
        queryset=ArmatureKlas.objects.all(),
        label="Класс арматуры"
    )

    armature_diameter = django_filters.ModelMultipleChoiceFilter(
        field_name='armature_diameter',
        queryset=Armature.objects.all(),
        label="Диаметр арматуры"
    )

    bar_type = django_filters.MultipleChoiceFilter(
        field_name='bar_type',
        choices=BaseArmature.ARMATURE_TYPE_CHOICES,
        label="Тип арматуры"
    )

    manufacture_place = django_filters.MultipleChoiceFilter(
        field_name='manufacture_place',
        choices=BaseArmature.MANUFACTURE_PLACE_CHOICES,
        label="Место изготовления"
    )


    @property
    def qs(self):
        # Получаем фильтруемые значения
        section = self.data.get('section')
        concrete = self.data.get('concrete')
        column = self.data.get('column')
        walls = self.data.get('wall')
        slab = self.data.get('slab')
        floor = self.data.get('floor')
        transition = self.data.get('transition')
        armature_klas = self.data.get('armature_klas')
        armature_diameter = self.data.get('armature_diameter')
        bar_type = self.data.get('bar_type')
        manufacture_place = self.data.get('manufacture_place')

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

        # Фильтрация по параметрам арматуры
        if armature_klas:
            armature_klas_list = self.data.getlist('armature_klas')
            cfs_qs = cfs_qs.filter(
                column__columnarmature__klas__in=armature_klas_list
            ).distinct("column")
            sfs_qs = sfs_qs.filter(
                slab__slabarmature__klas__in=armature_klas_list
            ).distinct('slab')
            tfs_qs = tfs_qs.filter(
                transition__transitionarmature__klas__in=armature_klas_list
            ).distinct('transition')
            wfs_qs = wfs_qs.filter(
                wall__wallarmature__klas__in=armature_klas_list
            ).distinct('wall')

            print(cfs_qs, "COLUMNS")

        if armature_diameter:
            armature_diameter_list = self.data.getlist('armature_diameter')
            cfs_qs = cfs_qs.filter(column__columnarmature__diameter__in=armature_diameter_list).distinct('column')
            sfs_qs = sfs_qs.filter(slab__slabarmature__diameter__in=armature_diameter_list).distinct('slab')
            tfs_qs = tfs_qs.filter(transition__transitionarmature__diameter__in=armature_diameter_list).distinct('transition')
            wfs_qs = wfs_qs.filter(wall__wallarmature__diameter__in=armature_diameter_list).distinct('wall')

        if bar_type:
            bar_type_list = self.data.getlist('bar_type')
            cfs_qs = cfs_qs.filter(column__columnarmature__bar_type__in=bar_type_list).distinct('column')
            sfs_qs = sfs_qs.filter(slab__slabarmature__bar_type__in=bar_type_list).distinct('slab')
            tfs_qs = tfs_qs.filter(transition__transitionarmature__bar_type__in=bar_type_list).distinct('transition')
            wfs_qs = wfs_qs.filter(wall__wallarmature__bar_type__in=bar_type_list).distinct('wall')

        if manufacture_place:
            manufacture_place_list = self.data.getlist('manufacture_place')
            cfs_qs = cfs_qs.filter(column__columnarmature__manufacture_place__in=manufacture_place_list).distinct('column')
            sfs_qs = sfs_qs.filter(slab__slabarmature__manufacture_place__in=manufacture_place_list).distinct('slab')
            tfs_qs = tfs_qs.filter(
                transition__transitionarmature__manufacture_place__in=manufacture_place_list).distinct('transition')
            wfs_qs = wfs_qs.filter(wall__wallarmature__manufacture_place__in=manufacture_place_list).distinct('wall')

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

        active_filters_t = {
            "bent": "гнутая",
            "straight": "прямая",
            'stock': 'Погонаж',
            'frame': 'Для каркасов',
            'factory': 'Завод',
            'site': 'Стройплощадка'
        }

        # Выбранные фильтры
        self.active_filters = {
            field.label: (
                field.queryset.filter(id__in=self.data.getlist(field_name))
                if hasattr(self.data, 'getlist') and hasattr(field, 'queryset') else
                [
                    active_filters_t.get(val, val)
                    for val in (self.data.getlist(field_name) if hasattr(self.data, 'getlist') else [])
                ]
            )
            for field_name, field in self.form.fields.items()
        }

        print("QS METHOD CALLED")

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
