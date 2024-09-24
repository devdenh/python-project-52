from django import forms

from task_manager.projects.models import Projects


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ['designation', 'name', 'change_number', 'issue_date']
        labels = {
            'designation': 'Обозначение',
            'name': 'Наименование',
            'change_number': 'Номер изменений',
            'issue_date': 'Дата выдачи'
        }
