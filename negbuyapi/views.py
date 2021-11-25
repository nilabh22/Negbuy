from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from .models import *
import random

# Create your views here.


@api_view(['GET'])
def login(request):
    user_id = request.headers['Authorization']
    phone_no = request.data['phone_no']
    return Response([user_id, phone_no], status=200)


@api_view(['GET'])
def featured_product(request):
    # Get User Id
    id = request.headers['Authorization']

    try:
        # Find User's City
        user_city = userdb.objects.get(id=id).city

        # Get all the products purchased in the region
        city_featured_products = order.objects.filter(
            user__city__exact=user_city)

        # Get the count for each product and the ids of top n products
        featured_products = city_featured_products.values(
            'product').annotate(count=Count('product')).order_by('-count')[:5]

        product_list_ = list()
        for featured_product in featured_products:
            each_product = product.objects.get(id=featured_product['product'])

            each_obj = {
                'id': each_product.id,
                'title': each_product.name,
                'price': each_product.price,
                'description': each_product.desc,
                'category': each_product.category_id.name,
                'image': '',
                'rating': {
                    'rate': 3.0,
                    'count': 430
                }
            }
            product_list_.append(each_obj)
        return Response(product_list_, status=200)

    except userdb.DoesNotExist:
        raise PermissionDenied()

# @api_view(['GET'])
# def product_list(request):
#     #in future will be changed according to user
#     #for now testing version
#     all_products = Product_db.objects.all()
#     product_list_ = list()
#     for each_product in all_products:
#         each_obj = {
#             'id':each_product.id,
#             'title':each_product.title,
#             'price':each_product.price,
#             'description':each_product.description,
#             'category':None,
#             'image':each_product.image.url,
#             'rating':{
#                 'rate':3.0,
#                 'count':430
#             }
#         }
#         product_list_.append(each_obj)
#     return Response(product_list_, status=200)


# @api_view(['GET'])
# def mostvalued_fastdispatch(request):
#     #in future will be changed according to user
#     #for now testing version
#     all_products = list(Product_db.objects.all())
#     Most_valued_product = random.sample(all_products, 4)
#     most_valued = list()
#     fast_dispatch = list()
#     for i in Most_valued_product:
#         qwe = {
#             'id':i.id,
#             'title':i.title,
#             'price':i.price,
#             'description':i.description,
#             'category':None,
#             'image':i.image.url,
#             'rating':{
#                 'rate':3.0,
#                 'count':430
#             }
#         }
#         most_valued.append(qwe)
#     for i in all_products:
#         if len(fast_dispatch) < 4:
#             if i.fast_dispatch == 'True':
#                 qwe = {
#                     'id':i.id,
#                     'title':i.title,
#                     'price':i.price,
#                     'description':i.description,
#                     'category':None,
#                     'image':i.image.url,
#                     'rating':{
#                         'rate':3.0,
#                         'count':430
#                     }
#                 }
#                 fast_dispatch.append(qwe)
#         else:
#             break
#     return Response({'Most_valued':most_valued, 'fast_dispatch':fast_dispatch}, status=200)
