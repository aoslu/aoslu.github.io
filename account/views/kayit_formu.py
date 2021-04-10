#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms.kayit_formu import KayitForm
from django.contrib.auth import login, authenticate

#@login_required(login_url='/')
def kayit_formu(request):
    if request.method=='POST':
        form = KayitForm(request.POST)
        if form.is_valid():
           form.save()
           username= form.cleaned_data.get('username')
           password= form.cleaned_data.get('password1')
           user= authenticate(username=username,  password= password)
           login(request, user)
           messages.success(request, 'Kayıt Başarılı')
           return redirect('anasayfa')
    else:
        form = KayitForm()
    return render(request, "ev/kayit_formu.html",context={'form':form})


