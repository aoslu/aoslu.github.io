from django.db import models

class YorumModel(models.Model):
    yazan= models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE,related_name='yorum')
    yorum = models.TextField()
    olusturulma_tarihi= models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi= models.DateTimeField(auto_now=True)

    class Meta:
        db_table='yorum'
        verbose_name='Yorum'
        verbose_name_plural='yorumlar'