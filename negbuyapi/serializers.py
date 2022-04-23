from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImages
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    # product_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = product
        fields = [
            'name',
            'sku',
            'category_id',
            'inventory_id',
            'featured_products',
            'best_selling_products',
            'hot_selling_products',
            'main_image',
            'fast_dispatch',
            'ready_to_ship',
            'customized_product',
            'brand',
            'keyword',
            'color',
            'size',
            'details',
            'price_choice',
            'price',
            'mrp',
            'sale_price',
            'sale_startdate',
            'sale_enddate',
            'manufacturing_time',
            'quantity_price',
            'maximum_order_quantity',
            'weight',
            'transportation_port',
            'packing_details',
            'packing_address',
            'status',
            # 'created_at',
            # 'modified_at',
            # 'deleted_at',
            # 'product_images'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = [
            'order_time',
            'order_quantity',
            'shipping_date',
            'delivery_date',
            'status',
            'feedback',
            'order_note'
        ]


class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = port
        fields = [
            'name',
            'country',
            'latitude',
            'longitude'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDB
        fields = [
            'user_id',
            'username',
            'first_name',
            'phone',
            'email',
        ]
