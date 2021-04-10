from django import forms
from deneme.models import MessageModel

class MessageForm(forms.ModelForm):
    class Meta:
        model= MessageModel
        fields= ('name','email','message','mesajgonderen')

