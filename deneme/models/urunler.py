from django.db import models
from deneme.models import KategoriModel

class ProductModel(models.Model):
    foto_ekle= models.ImageField(upload_to='urun_resimleri',blank=True, null=True)
    baslik= models.CharField(max_length= 50)
    fiyat_ekle=models.SmallIntegerField()
    aciklama= models.CharField(max_length=350)
    olusturulma_tarihi= models.DateTimeField(auto_now_add=True)
    kategoriler= models.ManyToManyField(KategoriModel, related_name= 'urun')
    yazar= models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='urunler', null= True)

    class Meta:
        db_table= 'urunler'
        verbose_name='Ürün'
        verbose_name_plural='Ürünler'

    def __str__(self):
        return self.baslik
