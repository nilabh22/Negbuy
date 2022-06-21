from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImages
        fields = ['image']

<<<<<<< HEAD
    def to_representation(self, instance):
        json_obj = super().to_representation(instance)
        image_list = []
        image_list = json_obj['image']

        return image_list


class product_serializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ['name', 'brand', 'price', 'sku', 'id', 'varients']


class InventorySerializer(serializers.ModelSerializer):
    product = product_serializer(read_only=True)

    class Meta:
        model = Inventory
        fields = '__all__'

    def to_representation(self, instance):
        json_obj = super().to_representation(instance)
        product_images = productImages.objects.filter(
            product=json_obj['product']['id'], color=json_obj['color'])
        image_serialized = ImageSerializer(product_images, many=True).data
        json_obj['images'] = []
        for image in image_serialized:
            json_obj['images'].append(image)

        varients = {
            "images": json_obj['images'],
            "size": json_obj['size'],
            "color": json_obj['color'],
            "quantity": json_obj['quantity']
        }
        json_obj['varients'] = varients
        del json_obj['images'], json_obj['size'], json_obj['quantity'], json_obj['color']

        return json_obj['varients']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDB
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'profile_picture'
        ]

    def to_representation(self, instance):
        json_obj = super().to_representation(instance)
        for k in json_obj:
            if json_obj[k] == None:
                json_obj[k] = ''
        return json_obj


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = productCategory
        fields = ['name']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_detail_db
        fields = ['heading', 'desc', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = review_db
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     reviews = {
    #         'rating': 4,
    #         'count': 220
    #     }
    #     return reviews


class ProductSerializer(serializers.ModelSerializer):
    product_images = ImageSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    category_id = CategorySerializer(read_only=True)
    image_details = ProductDetailSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = product
        fields = '__all__'

    def to_representation(self, instance):
        json_obj = super().to_representation(instance)
        try:
            json_obj['size'] = json_obj['size'].split(
                ',') if json_obj['size'] is not None else []

            json_obj['keyword'] = json_obj['keyword'].split(
                ',') if json_obj['keyword'] is not None else []

            json_obj['color'] = json_obj['color'].split(
                ',') if json_obj['color'] is not None else []

            json_obj['details'] = json_obj['details'].split(
                ',') if json_obj['details'] is not None else []

            json_obj['reviews'] = {'rating': 4, 'count': 220}
            retList = []
            if json_obj['details'] != []:
                for i in json_obj['details']:
                    obj = {}
                    newList = i.split(':')
                    obj['title'] = newList[0]
                    obj['description'] = newList[1]
                    retList.append(obj)

            json_obj['details'] = retList

            json_obj['category_id'] = json_obj['category_id']['name']
            json_obj['quantity_price'] = json_obj['quantity_price'].split(
                ',') if json_obj['quantity_price'] is not None else []
            for k in json_obj:
                if json_obj[k] == None or json_obj[k] == 'null':
                    json_obj[k] = ''

            return json_obj
        except Exception as e:
            return json_obj


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product_info = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = orders
        fields = '__all__'


class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = port
        fields = '__all__'
=======

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
            'created_at',
            'modified_at',
            'deleted_at',
            # 'product_images'
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = [
            'id',
            'order_number',
            'order_date',
            'order_time',
            'user',
            'product_info',
            'order_quantity',
            'shipping_date',
            'delivery_date',
            'status',
            'feedback'
        ]
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = product
#         fields = '__all__'
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
