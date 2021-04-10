from django import forms
from deneme.models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model= ProductModel
        fields=('foto_ekle', 'baslik','fiyat_ekle', 'aciklama', 'yazar', 'kategoriler')