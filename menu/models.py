from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuTree(MPTTModel):
    name_ru = models.CharField(max_length=50)
    name_kz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    icon = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return self.name_ru

    class MPTTMeta:
        order_insertion_by = ['name_ru']