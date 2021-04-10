from django import forms
from account.models import CustomUserModel

class CustomUserModelForm(forms.ModelForm):
    class Meta:
        model= CustomUserModel
        fields= ['username','password','email','adres','sehir', 'inputstate', 'postakodu']
        widgets={
            'username': forms.TextInput(attrs={'placeholder':'Ad/Soyad','class':'form-control'}),
            'password': forms.TextInput(attrs={'placeholder':'Mesajınız','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'Mailiniz','class':'form-control'}),
            'adres': forms.TextInput(attrs={'placeholder':'Adresiniz','class':'form-control'}),
            'sehir': forms.TextInput(attrs={'placeholder':'Şehriniz','class':'form-control'}),
            'inputstate': forms.TextInput(attrs={'class':'form-control'}),
            'postakodu': forms.TextInput(attrs={'placeholder':'Posta Kodu','class':'form-control'})
    }