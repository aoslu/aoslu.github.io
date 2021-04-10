from django.urls import path
from account.views import cikis, sifre_degistir, profil_guncelle, kayit_formu
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('giris',auth_views.LoginView.as_view(
        template_name='ev/giris.html'
        ),
        name="giris"),
    path('cikis/', cikis, name="cikis"),
    path('sifre-degistir/', sifre_degistir, name="sifredegistir"),
    path('profil-guncelle/', profil_guncelle, name="profil_guncelle"),
    path('kayit-formu/', kayit_formu, name="kayit_formu")
]
