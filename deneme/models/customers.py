from django.db import models

class Customers(models.Model):
    name= models.CharField(max_length=50)
    surname= models.CharField(max_length=50)
    puan= models.IntegerField()
    comment= models.CharField(max_length=50)

    class Meta:
        db_table='customer'
        verbose_name='Customer'
        verbose_name_plural='Customers'

    def __str__(self):
        return self.name