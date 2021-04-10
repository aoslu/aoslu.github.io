from django.db import models

class MessageModel(models.Model):
    name= models.CharField(max_length=60)
    email= models.EmailField(max_length=40)
    message= models.TextField(max_length=300)
    mesajgonderen= models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='mesajlar', null=True)

    class Meta:
        db_table= 'mesaj'
        verbose_name= 'Mesaj'
        verbose_name_plural='Mesajlar'

    def __str__(self):
        return self.name