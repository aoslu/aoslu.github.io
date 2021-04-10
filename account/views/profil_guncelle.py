from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import ProfilDuzenlemeForm

@login_required(login_url='/kayit_formu')
def profil_guncelle(request):
    if request.method=='POST':
        form = ProfilDuzenlemeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
           form.save()
           messages.success(request, 'Profil Güncellendi')
    else:
        form = ProfilDuzenlemeForm(instance = request.user)
    return render(request, "ev/profil_guncelle.html", context= {'form':form})