from django import forms

from task_manager.floors.models import Floor


class FloorForm(forms.ModelForm):

    class Meta:
        model = Floor
        fields = [
            'number', 'tier_number', 'floor_height', 'wall_height',
            'slab_thickness', 'section'
        ]
        labels = {
            'number': 'Номер этажа',
            'tier_number': 'Номер яруса',
            'floor_height': 'Высота вертикальных конструкций',
            'wall_height': 'Высота стен',
            'slab_thickness': 'Толщина перекрытий',
            'section': 'Секция'
        }
