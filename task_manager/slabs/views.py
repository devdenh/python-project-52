from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)

from task_manager.slabs.forms import SlabForm, SlabArmatureFormSet
from task_manager.slabs.models import Slab

REGISTRATION_SUCCESS_MESSAGE = "Slab created successfully"
UPDATE_SUCCESS_MESSAGE = "Slab updated successfully"
DELETE_SUCCESS_MESSAGE = "Slab deleted successfully"
LABEL_USED_MESSAGE = "You can't delete a slab that is still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Slab
    template_name = 'slabs/index.html'


class SlabDetail(DetailView):
    model = Slab
    template_name = "slabs/detail.html"
    extra_context = {"slabs": Slab.objects.all()}


class SlabInline:
    form_class = SlabForm
    model = Slab
    template_name = "slabs/create_or_update.html"

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
        return redirect('slabs:index')

    def formset_armatures_valid(self, formset):
        armatures = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for armature in armatures:
            armature.slab = self.object
            armature.save()


class SlabRegistrate(SlabInline, CreateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {'armatures': SlabArmatureFormSet(prefix='armatures')}
        else:
            return {
                'armatures': SlabArmatureFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix='armatures'
                )
            }


class SlabUpdate(SlabInline, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'armatures': SlabArmatureFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix='armatures'
            )
        }


class SlabDelete(LoginRequiredMixin,
                 SuccessMessageMixin,
                 DeleteView):
    model = Slab
    template_name = 'slabs/delete.html'
    success_url = reverse_lazy('slabs:index')
    success_message = DELETE_SUCCESS_MESSAGE
