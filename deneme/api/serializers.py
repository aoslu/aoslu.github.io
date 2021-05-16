from rest_framework import serializers
from deneme.models import ProductModel, KategoriModel, Customers

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields= '__all__'
        read_only_fields= ['id',]

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
        read_only_fields= ['id',]

class KategoriModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriModel
        fields = '__all__'
        read_only_fields= ['id',]
#standart serializer...........................................
# class CustomersDefaultSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     surname= serializers.CharField()
#     puan= serializers.IntegerField()
#     comment= serializers.CharField()

#     def create(self, validated_data):
#         print(validated_data)
#         return Customers.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name= validated_data.get('name', instance.name)
#         instance.surname= validated_data.get('surname', instance.surname)
#         instance.puan= validated_data.get('puan', instance.puan)
#         instance.comment= validated_data.get('comment', instance.comment)
#         instance.save()
#         return instance

# #VALİDATİON...
#     def validate(self, data):
#         if data['name'] == data['surname']:
#             raise serializers.ValidationError(
#                 'Ad ve Soyad Aynı Olamaz'
#             )
#         return data
#     def validate_name(self, value):
#         if len(value) < 5 :
#             raise serializers.ValidationError(
#                 f'İsminiz 5 haneden küçük olamaz. Siz {len(value)} karakter girdiniz'
#             )
#         return value
#class ProductModelSerializer(serializers.Serializer):
#    id= serializers.IntegerField(read_only=True)
#    foto_ekle= serializers.ImageField()
#    baslik= serializers.CharField()
#    fiyat_ekle=serializers.IntegerField()
#    aciklama= serializers.CharField()
#    olusturulma_tarihi= serializers.DateTimeField(read_only=True)
    #kategoriler= serializers.ManyToManyField(read_only=True)
    #yazar= serializers.ForeignKey(read_only=True)

#    def create(self, validated_data):
#        print(validated_data)
#        return ProductModel.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.foto_ekle= validated_data.get('foto_ekle', instance.foto_ekle)
        #instance.yazar= validated_data.get('yazar', instance.yazar)
#        instance.baslik = validated_data.get('baslik', instance.baslik)
#        instance.aciklama= validated_data.get('aciklama', instance.aciklama)
#        instance.fiyat_ekle= validated_data.get('fiyat_ekle', instance.fiyat_ekle)
#       instance.olusturulma_tarihi= validated_data.get('olusturulma_tarihi', instance.olusturulma_tarihi)
#        instance.kategoriler= validated_data.get('kategoriler', instance.kategoriler)
#        instance.save()
#        return instance
#-------------------------------------------------------------------------------------------------------
        # python manage.py shell_plus ( içinde belirli modeli veriye çevirip jsona çevirme...)
#from deneme.models import ProductModel
#from deneme.api.serializers import ProductModelSerializer

#urun = ProductModel.objects.first() -- İlk objeyi çekmeye yarar
#urun.baslik     --ProductModelSerializer içinden istediğimizveriyi çekme
#serializer = ProductModelSerializer(urun)
#pprint(serializer.data)  --datayı görme
#SERİALİZERDEN GELEN DATAYI JSONA ÇEVİRME BYTE FORMATINDA.......
#from rest_framework.renderers import JSONRenderer
#data = JSONRenderer().render(serializer.data)
#pprint(data)=>(b'{"id":8,"foto_ekle":"/media/urun_resimleri/arkakapak.png","baslik":"benialal' b'benial","fiyat_ekle":80,"aciklama":"benialalbenialllll","olusturulma_tarihi"' b':"2021-03-23T19:30:58.005451+03:00"}')
# type(data)  => bytes

# BURAYA KADAR OLAN HERŞEY SERİALİZATİON İŞLEMLERİ...

#byte olan veriyi parse etme
#import io
#from rest_framework.parsers import JSONParser

#data =>>> Out[24]: b'{"id":8,"foto_ekle":"/media/urun_resimleri/arkakapak.png","baslik":"benialalbenial","fiyat_ekle":80,"aciklama":"benialalbenialllll","olusturulma_tarihi":"2021-03-23T19:30:58.005451+03:00"}'
#stream = io.BytesIO(data)
#stream =><_io.BytesIO at 0x2e3f3c63ae0>

