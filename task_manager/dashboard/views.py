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


# class IndexView(LoginRequiredMixin,
#                 FilterView):
#     model = Dashboard
#     template_name = 'dashboard/index.html'
#     filterset_class = DashboardFilterForm
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["filter"] = DashboardFilterForm(self.request.GET,
#                                                 queryset=self.get_queryset())
#         return context


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

        context['filter'] = filter_set
        context['constructions'] = page_obj  # Используем объекты страницы вместо полного списка
        context['active_filters'] = filter_set.active_filters
        context['total_volume'] = filter_set.calculate_total_volume()
        context['page_obj'] = page_obj  # Добавляем объект страницы в контекст

        return context

# class DetailTask(DetailView):
#     model = Dashboard
#     template_name = "dashboard/detail.html"
    # extra_context = {"labels": Label.objects.all()}


# class TaskRegistrate(LoginRequiredMixin,
#                      SuccessMessageMixin,
#                      CreateView):
#
#     model = Task
#     form_class = TaskForm
#     template_name = 'tasks/create.html'
#     success_url = reverse_lazy('tasks:index')
#     success_message = REGISTRATION_SUCCESS_MESSAGE
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class TaskUpdate(LoginRequiredMixin,
#                  SuccessMessageMixin,
#                  UpdateView):
#
#     model = Task
#     form_class = TaskForm
#     template_name = 'tasks/update.html'
#     success_url = reverse_lazy('tasks:index')
#     success_message = UPDATE_SUCCESS_MESSAGE
#
#
# class TaskDelete(LoginRequiredMixin,
#                  UserPassesTestMixin,
#                  SuccessMessageMixin,
#                  DeleteView):
#
#     model = Task
#     template_name = 'tasks/delete.html'
#     success_url = reverse_lazy('tasks:index')
#     success_message = DELETE_SUCCESS_MESSAGE
#
#     def test_func(self):
#         return self.request.user.id == self.get_object().author.id
#
#     def handle_no_permission(self):
#         messages.error(self.request, NOT_AUTHOR_MESSAGE)
#         return redirect(reverse_lazy('tasks:index'))
