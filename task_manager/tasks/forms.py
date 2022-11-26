from django.utils.translation import gettext as _
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.labels.models import Label
from django import forms
import django_filters


class TaskForm(forms.ModelForm):

    name = forms.CharField(label=_("Name"),
                           required=True)

    description = forms.Textarea()

    status = forms.ModelChoiceField(label=_("Status"),
                                    queryset=Statuses.objects.all())

    executor = forms.ModelChoiceField(label=_("Executor"),
                                      initial="",
                                      empty_label="",
                                      queryset=User.objects.all(),
                                      required=False)

    label = forms.ModelMultipleChoiceField(label=_("Label"),
                                           queryset=Label.objects.all(),
                                           required=False)

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "label"]


class FilterForm(django_filters.FilterSet):

    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all()
    )

    author_only = django_filters.BooleanFilter(
        field_name="self_tasks",
        label=_("Only author tasks"),
        method="owner_filter",
        widget=forms.CheckboxInput
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "label"]

    def owner_filter(self, queryset, name, value):
        if value:
            return queryset.filter(author_id=self.request.user.id)
        return queryset
