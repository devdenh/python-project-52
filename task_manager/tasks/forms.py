from django.utils.translation import gettext as _
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.labels.models import Label
from django import forms


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
