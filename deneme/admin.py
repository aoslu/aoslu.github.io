from django.contrib import admin
from deneme.models import KategoriModel, ProductModel, AltKategoriModel, MessageModel
from deneme.models.urun_yorum import YorumModel
# Register your models here.

admin.site.register(KategoriModel)


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display= ('baslik', 'fiyat_ekle', 'aciklama', 'olusturulma_tarihi', 'foto_ekle',)
    search_fields= ('baslik', 'aciklama')

@admin.register(AltKategoriModel)
class AltKategoriModelAdmin(admin.ModelAdmin):
    list_display = ('isim',)
    search_fields= ('isim',)

admin.site.register(MessageModel)

class YorumAdmin(admin.ModelAdmin):
    list_display= ('yazan','olusturulma_tarihi','guncellenme_tarihi')
    search_fields= ('yazan__username',)

admin.site.register(YorumModel, YorumAdmin)