from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from task_manager.walls.forms import WallForm, WallArmatureFormSet
from task_manager.walls.models import Wall

class IndexView(LoginRequiredMixin, ListView):
    model = Wall
    template_name = 'walls/index.html'


class WallDetail(DetailView):
    model = Wall
    template_name = "walls/detail.html"
    extra_context = {"walls": Wall.objects.all()}


class WallInline():
    form_class = WallForm
    model = Wall
    template_name = "walls/create_or_update.html"

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
        return redirect('walls:index')

    def formset_armatures_valid(self, formset):
        armatures = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for armature in armatures:
            armature.wall = self.object
            armature.save()


class WallRegistrate(WallInline, CreateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {'armatures': WallArmatureFormSet(prefix='armatures')}
        else:
            return {
                'armatures': WallArmatureFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix='armatures'
                )
            }


class WallUpdate(WallInline, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'armatures': WallArmatureFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix='armatures'
            )
        }


class WallDelete(LoginRequiredMixin, DeleteView):
    model = Wall
    template_name = 'walls/delete.html'
    success_url = reverse_lazy('walls:index')
