from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic import (
    ListView
)

from task_manager.columns.forms import ColumnForm, ColumnArmatureFormSet
from task_manager.columns.models import Column

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Column
    template_name = 'columns/index.html'


class ColumnDetail(DetailView):
    model = Column
    template_name = "columns/detail.html"
    extra_context = {"columns": Column.objects.all()}


class ColumnInline:
    form_class = ColumnForm
    model = Column
    template_name = "columns/create_or_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, f'formset_{name}_valid', None)
            if formset_save_func:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('columns:index')

    def formset_armatures_valid(self, formset):
        armatures = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for armature in armatures:
            armature.column = self.object
            armature.save()

class ColumnRegistrate(ColumnInline, CreateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {'armatures': ColumnArmatureFormSet(prefix='armatures')}
        else:
            return {
                'armatures': ColumnArmatureFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix='armatures'
                )
            }

class ColumnUpdate(ColumnInline, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'armatures': ColumnArmatureFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix='armatures'
            )
        }

class ColumnDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Column
    template_name = 'columns/delete.html'
    success_url = reverse_lazy('columns:index')
    success_message = "Колонна успешно удалена."
