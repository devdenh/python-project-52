from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.translation import gettext as _
from django.views.generic import ListView
from django_filters.views import FilterView

from task_manager.dashboard.forms import DashboardFilterForm
from task_manager.dashboard.models import Dashboard
from task_manager.tasks.models import Task

REGISTRATION_SUCCESS_MESSAGE = _("Task created Successfully")
UPDATE_SUCCESS_MESSAGE = _("Task updated Successfully")
DELETE_SUCCESS_MESSAGE = _("Task deleted Successfully")
NOT_AUTHOR_MESSAGE = _("Only author can delete this task")


class IndexView(LoginRequiredMixin,
                FilterView):
    model = Task
    template_name = 'dashboard/index.html'
    filterset_class = DashboardFilterForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = DashboardFilterForm(self.request.GET,
                                                queryset=self.get_queryset())
        return context


class DashboardView(LoginRequiredMixin,
                    FilterView):
    model = Dashboard  # Используем связь как основную модель
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'results'
    filterset_class = DashboardFilterForm

    def get_queryset(self):
        queryset = super().get_queryset()

        # Получаем данные фильтров из GET-запроса
        section = self.request.GET.get('section')
        floor = self.request.GET.get('floor')
        concrete = self.request.GET.get('concrete')
        project = self.request.GET.get('project')
        column = self.request.GET.get('column')
        wall = self.request.GET.get('wall')
        slab = self.request.GET.get('slab')

        # Применение фильтров
        if section:
            queryset = queryset.filter(section__id=section)
        if floor:
            queryset = queryset.filter(floor__id=floor)
        if concrete:
            queryset = queryset.filter(concrete__id=concrete)
        if project:
            queryset = queryset.filter(
                Q(column__project__id=project) | Q(wall__project__id=project) | Q(slab__project__id=project))
        if column:
            queryset = queryset.filter(column__id=column)
        if wall:
            queryset = queryset.filter(wall__id=wall)
        if slab:
            queryset = queryset.filter(slab__id=slab)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаем форму фильтров в контекст
        context['filter_form'] = DashboardFilterForm(self.request.GET or None)
        return context


# class DetailTask(DetailView):
#     model = Task
#     template_name = "tasks/detail.html"
#     extra_context = {"labels": Label.objects.all()}
#
#
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
