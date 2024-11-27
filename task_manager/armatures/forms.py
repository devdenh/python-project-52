from django import forms

from task_manager.armatures.models import Armature


class ArmatureForm(forms.ModelForm):

    class Meta:
        model = Armature
        fields = [
            'linear_weight', 'diameter'
        ]
        labels = {
            'linear_weight': 'Масса погонного метра',
            'diameter': 'Диаметр'
        }