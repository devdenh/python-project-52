from django.db import models
from django.urls import reverse_lazy


class Concrete(models.Model):
    klas = models.CharField(max_length=255)
    marka = models.CharField(max_length=255)
    strength_mpa  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # # Связь с другими моделями
    # column_concrete = models.ManyToManyField('ColumnConcrete', blank=True)
    # slab_concrete = models.ManyToManyField('SlabConcrete', blank=True)
    # stair_slab_concrete = models.ManyToManyField('StairSlabConcrete', blank=True)
    # wall_concrete = models.ManyToManyField('WallConcrete', blank=True)

    def get_absolute_url(self):
        return reverse_lazy('concrete:index')

    def __str__(self):
        return f"{self.klas}"
