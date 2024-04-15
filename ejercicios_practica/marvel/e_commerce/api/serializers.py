
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import *
from django.contrib.auth.models import User

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers


class ComicSerializer(serializers.ModelSerializer):
    # new_field = serializers.SerializerMethodField()

    # def get_new_field(self, obj):
    #     return {'message': 'Acá puedo devolver más información.'}

    user_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=User.objects.all())   
    
    comic_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                                  many=True,
                                                  queryset=WishList.objects.all())   

    class Meta:
        model = Comic
        #fields = '__all__'
        fields = ('id','marvel_id', 'title', 'description','price','stock_qty','picture', 'user_id','comic_id')
        read_only_fields = ('id',)


# TODO: Realizar el serializador para el modelo de User y WishList
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id', 'username', 'email')
        read_only_fields = ('id',)


class WishListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WishList
        fields = '__all__'
        read_only_fields = ('id',)

