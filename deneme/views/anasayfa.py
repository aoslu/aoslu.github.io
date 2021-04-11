from django.shortcuts import render, get_object_or_404
from deneme.models import AltKategoriModel, ProductModel, YorumModel
from django.core.paginator import Paginator
from deneme.forms import MessageForm, YorumModelForm
# ProductForm,
from django.db.models import Q
from django.views.generic import CreateView
#from django.contrib.auth.decorators import login_required
from django.urls import reverse


def anasayfa(request):
    sorgu = request.GET.get('sorgu')
    alt_kategoriler= AltKategoriModel.objects.all()
    urunler= ProductModel.objects.all()
    if sorgu:  #SearchBox Kutusu İşlev Kodu
        urunler = urunler.filter(
            Q(baslik__icontains=sorgu) |
            Q(aciklama__icontains=sorgu)
        ).distinct()

    sayfa = request.GET.get('sayfa')
    paginator = Paginator(urunler, 6) # Sayfalama Kısmı

    if request.method == 'POST':
        form= MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm() #MessageForm
    else:
        form = MessageForm()
    return render(request, "ev/anasayfa.html", context={'alt_kategoriler':alt_kategoriler, 'urunler':paginator.get_page(sayfa), 'form':form})

class UrunEkleCreateView(CreateView):
    template_name= 'ev/urun_ekle.html'
    model= ProductModel
    fields= ('baslik', 'foto_ekle', 'fiyat_ekle', 'aciklama')
    def get_success_url(self):
        return reverse('detay')

    def form_valid(self, form):
        urunler = form.save(commit=False)
        urunler.yazar = self.request.user
        urunler.save()
        form.save_m2m()
        return super().form_valid(form)

def contak(request):
    if request.method == 'POST':
        form= MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
    else:
        form = MessageForm()
    return render(request, "ev/contak.html", {'form':form})

def detay(request):
    if request.method=='POST':
        form= YorumModelForm(request.POST)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.yazar= request.user
            yorum.save()
    else:
        form=YorumModelForm()
    return render(request, "ev/detay.html", {'form':form})

def profil(request):
    return render(request, "ev/profil.html")

def girispaneli(request):
    return  render(request, "ev/girispaneli.html")

def brand(request):
    return render(request, "ev/brand.html")

def about(request):
    return render(request, "ev/about.html")

def special(request):
    return render(request, "ev/special.html")

def contact(request):
    return render(request, "ev/contact.html")

def sale(request):
    return render(request, "ev/sale.html")

def mesaj(request):
    return render(request, "ev/mesaj.html")