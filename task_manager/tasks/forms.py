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

    description = forms.CharField(label=_("Description"),
                                  required=False,
                                  widget=forms.Textarea())

    status = forms.ModelChoiceField(label=_("Status"),
                                    queryset=Statuses.objects.all(),
                                    required=True)

    executor = forms.ModelChoiceField(label=_("Executor"),
                                      initial="---------",
                                      empty_label="---------",
                                      queryset=User.objects.all(),
                                      required=False,
                                      widget=forms.Select())

    labels = forms.ModelMultipleChoiceField(label=_("Labels"),
                                            label_suffix="",
                                            initial=None,
                                            show_hidden_initial=False,
                                            queryset=Label.objects.all(),
                                            required=False)

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]


class FilterForm(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        field_name="status",
        queryset=Statuses.objects.all(),
        label=_("Status")
    )

    executor = django_filters.ModelChoiceFilter(
        field_name="executor",
        queryset=User.objects.all(),
        label=_("Executor")
    )

    label = django_filters.ModelChoiceFilter(
        field_name="labels",
        queryset=Label.objects.all(),
        label=_("Label")
    )

    author_only = django_filters.BooleanFilter(
        field_name="self_tasks",
        label=_("Only author tasks"),
        label_suffix="",
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
