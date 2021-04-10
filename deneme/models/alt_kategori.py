from django.db import models
from deneme.models import KategoriModel

class AltKategoriModel(models.Model):
    isim= models.CharField(max_length=50)
    kategoriler = models.ManyToManyField(KategoriModel, related_name= 'alturun')

    class Meta:
        db_table='alt_kategori'
        verbose_name='Kategori'
        verbose_name_plural='Alt_Kategoriler'

    def __str__(self):
        return self.isim
