from django.urls import path
from deneme.api import views as api_views

urlpatterns = [
  #  path('urunlerim/', api_views.urun_list_create_api_view, name= 'urun-listesi')
    path('customers/', api_views.CustomerListCreateAPIView.as_view(), name= 'musteri-listesi'),
    path('customers/<int:pk>', api_views.CustomerDetailAPIView.as_view(), name= 'musteri-listesi-detay'),
]


# FUNCTİON BASED VİEWS
# urlpatterns = [
#   #  path('urunlerim/', api_views.urun_list_create_api_view, name= 'urun-listesi')
#     path('customers/', api_views.customer_list_create_api_view, name= 'musteri-listesi'),
#     path('customers/<int:pk>', api_views.customer_detail_api_view, name= 'musteri-listesi-detay'),
# ]