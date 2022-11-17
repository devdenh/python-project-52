from task_manager.statuses.models import Statuses
from django import forms


class StatusesForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = ['name']
