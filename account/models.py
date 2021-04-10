from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    avatar= models.ImageField(upload_to= 'avatar/', blank= True, null=True)
    adres = models.CharField(max_length=200)
    sehir=models.TextField()
    inputstate= models.TextField()
    postakodu= models.TextField()

    class Meta:
        db_table='user'
        verbose_name='Kullanıcı'
        verbose_name_plural='Kullanıcılar'

    def __str__(self):
        return self.username


