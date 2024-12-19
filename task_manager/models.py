from django.db import models

from task_manager.armatures.models import Armature
from task_manager.armaturesklas.models import ArmatureKlas


class BaseArmature(models.Model):
    ARMATURE_TYPE_CHOICES = [
        ('bent', 'Гнутый'),
        ('straight', 'Прямой'),
        ('stock', 'Погонаж'),
        ('frame', 'Для каркасов'),
    ]

    MANUFACTURE_PLACE_CHOICES = [
        ('factory', 'Завод'),
        ('site', 'Стройплощадка'),
    ]

    diameter = models.ForeignKey(Armature, on_delete=models.CASCADE)  # Диаметр, mm
    klas = models.ForeignKey(ArmatureKlas, on_delete=models.CASCADE)  # Класс
    bar_length = models.FloatField()  # Длина стержней
    bar_count = models.IntegerField()  # Кол-во стержней
    bar_type = models.CharField(max_length=20, choices=ARMATURE_TYPE_CHOICES)  # Вид стержня
    manufacture_place = models.CharField(max_length=20, choices=MANUFACTURE_PLACE_CHOICES)  # Место изготовления

    class Meta:
        abstract = True

    def __str__(self):
        return f"Арматура {self.diameter}mm, {self.klas}"


class ArmatureMassCalculationMixin:
    def calculate_armature_mass(self, armature_model, foreign_key_name):
        """
        Вычислить общую массу арматуры для связанных объектов.

        :param armature_model: Модель арматуры (например, TransitionArmature)
        :param foreign_key_name: Название внешнего ключа, связывающего основную модель с моделью арматуры
        :return: Общая масса арматуры
        """
        # Получаем связанные объекты арматуры
        filter_kwargs = {foreign_key_name: getattr(self, foreign_key_name)}
        armatures = armature_model.objects.filter(**filter_kwargs)

        # Рассчитываем и суммируем массу арматуры
        total_mass = sum(
            armature.diameter.linear_weight * armature.bar_length * armature.bar_count
            for armature in armatures if armature.diameter and armature.bar_length and armature.bar_count
        )
        return total_mass
