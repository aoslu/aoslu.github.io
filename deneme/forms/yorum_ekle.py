from django import forms
from deneme.models import YorumModel

class YorumModelForm(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields=('yorum',)