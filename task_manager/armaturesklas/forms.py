from django import forms

from task_manager.armaturesklas.models import ArmatureKlas


class ArmatureKlasForm(forms.ModelForm):

    class Meta:
        model = ArmatureKlas
        fields = [
            'klas'
        ]
        labels = {
            'klas': 'Класс'
        }