from django.urls import path
from deneme.views import anasayfa, mesaj, UrunEkleCreateView ,profil, girispaneli, about, special, detay, sale, brand
from django.views.generic import TemplateView
urlpatterns = [
    path('', girispaneli, name="girispaneli"),
    path('anasayfa/',anasayfa, name="anasayfa"),
    path('brand/', brand, name="brand"),
    path('about/', about, name="about"),
    path('special/', special, name="special"),
    path('contact/', TemplateView.as_view(template_name='ev/contak.html'), name="contact"),
    path('detay/', detay, name="detay"),
    path('sale/', sale, name="sale"),
    path('profil/', profil, name="profil"),
    path('mesaj/', mesaj, name="mesaj"),
    path('urun_ekle/', UrunEkleCreateView.as_view() , name="urun_ekle"),
]