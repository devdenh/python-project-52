from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView, CreateView
from django_filters.views import FilterView

from task_manager.dashboard.forms import DashboardFilterForm
from task_manager.dashboard.models import Dashboard
from task_manager.tasks.models import Task

REGISTRATION_SUCCESS_MESSAGE = _("Task created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Task updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Task deleted Successfully")
NOT_AUTHOR_MESSAGE = _("Only author can delete this task")


class DashboardView(LoginRequiredMixin, FilterView):
    model = Dashboard
    template_name = 'dashboard/dashboard.html'
    filterset_class = DashboardFilterForm
    paginate_by = 20  # Количество элементов на странице

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Передаем форму фильтров в контекст
        filter_set = DashboardFilterForm(self.request.GET, queryset=self.get_queryset())
        constructions = filter_set.qs

        # Пагинация
        paginator = Paginator(constructions, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Общая масса арматуры
        total_mass = sum(construction.calculate_armature_mass() for construction in page_obj)

        context['filter'] = filter_set
        context['constructions'] = page_obj  # Используем объекты страницы вместо полного списка
        context['active_filters'] = filter_set.active_filters
        context['total_volume'] = filter_set.calculate_total_volume()
        context['total_mass'] = total_mass  # Общая масса арматуры
        context['page_obj'] = page_obj  # Добавляем объект страницы в контекст
        print("VIEW CALLED")

        return context
