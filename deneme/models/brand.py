from django.db import models
from django.db.models.fields import CharField
#from deneme.models import TypeModel

class BrandModel(models.Model):
    brand = models.CharField(max_length=100)
#    type_category = models.ManyToManyField(TypeModel, related_name="types")
    
    class Meta:
        db_table='brands'
        verbose_name='Brand'
        verbose_name_plural='Brands'


    def __str__(self):
        return self.brand