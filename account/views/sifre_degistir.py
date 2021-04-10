from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/kayit_formu')
def sifre_degistir(request):
    if request.method== 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user= form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifre Başarıyla Güncellendi')
            return redirect('sifredegistir')

    else:
        form = PasswordChangeForm(user= request.user)
    context = {
        'form':form
    }
    return render(request, "ev/sifre_degistir.html", context)


