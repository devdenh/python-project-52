from django import forms

from task_manager.slabs.models import Slab


class SlabForm(forms.ModelForm):

    class Meta:
        model = Slab
        fields = [
            'name', 'volume', 'thickness'
        ]
        labels = {
            'name': 'Наименование перекрытия',
            'volume': 'Объем',
            'thickness': 'Толщина'
        }
