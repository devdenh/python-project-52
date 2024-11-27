from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.views.generic.edit import ModelFormMixin
from django.contrib import messages

from task_manager.transitions.forms import TransitionForm, TransitionArmatureFormSet, TransitionArmatureForm
from task_manager.transitions.models import Transition, TransitionArmature

REGISTRATION_SUCCESS_MESSAGE = "Concrete created Successfully"
UPDATE_SUCCESS_MESSAGE = "Concrete updated Successfully"
DELETE_SUCCESS_MESSAGE = "Concrete deleted Successfully"
LABEL_USED_MESSAGE = "You can't delete Concrete are still being used"


class IndexView(LoginRequiredMixin,
                ListView):
    model = Transition
    template_name = 'transitions/index.html'


class TransitionBaseView(LoginRequiredMixin, SuccessMessageMixin, ModelFormMixin):
    model = Transition
    form_class = TransitionForm
    template_name = None # To be defined in the subclasses
    success_url = None  # To be defined in the subclasses
    success_message = None  # To be defined in the subclasses

    def get_formset(self):
        """Creates the inline formset for TransitionArmature."""
        if self.request.POST:
            return TransitionArmatureFormSet(self.request.POST, instance=self.object)
        return TransitionArmatureFormSet(instance=self.object)

    def get_context_data(self, **kwargs):
        """Adds the formset to the context."""
        context = super().get_context_data(**kwargs)
        context['armature_formset'] = kwargs.get('armature_formset', self.get_formset())
        return context

    def form_valid(self, form):
        print(self.request.POST)
        """Handles form and formset validation."""
        context = self.get_context_data()
        armature_formset = context['armature_formset']

        for frm in armature_formset:
            print(frm.errors, "OSIBKI FORMSETA")

        if armature_formset.is_valid():
            response = super().form_valid(form)
            armature_formset.instance = self.object
            armature_formset.save()
            return response
        else:
            return self.form_invalid(form)


    def form_invalid(self, form):
        # Обработка невалидной формы, возвращаем ошибки
        messages.error(self.request, "There was an error in the form.")
        print(form.errors.__dict__, "OSHIBKI")
        return self.render_to_response(self.get_context_data(form=form))



class TransitionRegistrate(TransitionBaseView, CreateView):
    model = Transition
    form_class = TransitionForm
    template_name = "transitions/create.html"
    success_url = reverse_lazy('transitions:index')
    success_message = "Лестничная площадка успешно создана."


class TransitionUpdate(TransitionBaseView, UpdateView):
    template_name = "transitions/update.html"
    success_url = reverse_lazy('transitions:index')
    success_message = "Лестничная площадка успешно обновлена."

    def form_valid(self, form):
        return super().form_valid(form)

    def get_formset(self):
        """Creates the inline formset for TransitionArmature."""
        ArmatureFormSet = inlineformset_factory(
            Transition,
            TransitionArmature,
            form=TransitionArmatureForm,
            extra=0,  # Убираем создание пустых форм
            can_delete=True
        )
        if self.request.POST:
            return ArmatureFormSet(self.request.POST, instance=self.object)
        return ArmatureFormSet(instance=self.object)


class TransitionDelete(TransitionBaseView, DeleteView):
    template_name = 'transitions/delete.html'
    success_url = reverse_lazy('transitions:index')
    success_message = DELETE_SUCCESS_MESSAGE
