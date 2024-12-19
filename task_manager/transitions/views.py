from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)

from task_manager.transitions.forms import TransitionForm, TransitionArmatureFormSet
from task_manager.transitions.models import Transition

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Transition
    template_name = 'transitions/index.html'


class DetailTransition(DetailView):
    model = Transition
    template_name = "transitions/detail.html"
    extra_context = {"transitions": Transition.objects.all()}


class TransitionInline():
    form_class = TransitionForm
    model = Transition
    template_name = "transitions/create_or_update.html"

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
        return redirect('transitions:index')

    def formset_armatures_valid(self, formset):
        armatures = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for armature in armatures:
            armature.transition = self.object
            armature.save()


class TransitionRegistrate(TransitionInline, CreateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {'armatures': TransitionArmatureFormSet(prefix='armatures')}
        else:
            return {
                'armatures': TransitionArmatureFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix='armatures'
                )
            }


class TransitionUpdate(TransitionInline, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'armatures': TransitionArmatureFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix='armatures'
            )
        }


class TransitionDelete(LoginRequiredMixin,
                 SuccessMessageMixin,
                 DeleteView):
    model = Transition
    template_name = 'transitions/delete.html'
    success_url = reverse_lazy('transitions:index')
    success_message = DELETE_SUCCESS_MESSAGE
