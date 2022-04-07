from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImages
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True)

    class Meta:
        model = product
        fields = '__all__'
