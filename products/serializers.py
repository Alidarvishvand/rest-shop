from rest_framework import serializers
from .models import Product,Post

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class Postserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'