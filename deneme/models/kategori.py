from django.db import models

class KategoriModel(models.Model):
    isim = models.CharField( max_length=40, blank=False,null=False)

    class Meta:
        db_table='kategori'
        verbose_name='Kategori'
        verbose_name_plural='Kategoriler'

    def __str__(self):
        return self.isim