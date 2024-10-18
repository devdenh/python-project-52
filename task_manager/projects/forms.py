from django import forms

from task_manager.projects.models import Project


class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['designation', 'name', 'change_number', 'issue_date']
        labels = {
            'designation': 'шифр проекта',
            'name': 'Наименование',
            'change_number': 'Номер изменений',
            'issue_date': 'Дата выдачи'
        }
