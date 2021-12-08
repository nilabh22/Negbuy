from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import random


def makeObject(product):
    object = {
        'name': product.name,
        'description': product.desc,
        'price': product.price,
        'category': product.category_id.name,
        'image': '',
        'rating': {
            'rate': 3.0,
            'count': 430
        }
    }
    return object


@api_view(['GET'])
def featured_product_api(request):
    featured_product_list = []
    featured_products = product.objects.filter(featured_products=True)[:10]
    for each_product in featured_products:
        featured_product_list.append(makeObject(each_product))

    if len(featured_product_list) != 10:
        products = list(product.objects.filter(featured_products=False))
        random_products = random.sample(
            products, 10-len(featured_product_list))
        for each_product in random_products:
            featured_product_list.append(makeObject(each_product))

    return Response(featured_product_list, status=200)


@api_view(['GET'])
def fast_dispatch_api(request):
    fast_dispatch_list = []
    fast_dispatch_products = product.objects.filter(fast_dispatch=True)[:10]
    for each_product in fast_dispatch_products:
        fast_dispatch_list.append(makeObject(each_product))

    if len(fast_dispatch_list) != 10:
        products = list(product.objects.filter(fast_dispatch=False))
        random_products = random.sample(
            products, 10-len(fast_dispatch_list))
        for each_product in random_products:
            fast_dispatch_list.append(makeObject(each_product))
    return Response(fast_dispatch_list, status=200)


@api_view(['GET'])
def ready_to_ship_api(request):
    ready_to_ship_list = []
    ready_to_ship_products = product.objects.filter(ready_to_ship=True)[:10]
    for each_product in ready_to_ship_products:
        ready_to_ship_list.append(makeObject(each_product))

    if len(ready_to_ship_list) != 10:
        products = list(product.objects.filter(ready_to_ship=False))
        random_products = random.sample(
            products, 10-len(ready_to_ship_list))
        for each_product in random_products:
            ready_to_ship_list.append(makeObject(each_product))
    return Response(ready_to_ship_list, status=200)


@api_view(['GET'])
def customized_product_api(request):
    customized_product_list = []
    customized_products = product.objects.filter(customized_product=True)[:10]
    for each_product in customized_products:
        customized_product_list.append(makeObject(each_product))

    if len(customized_product_list) != 10:
        products = list(product.objects.filter(customized_product=False))
        random_products = random.sample(
            products, 10-len(customized_product_list))
        for each_product in random_products:
            customized_product_list.append(makeObject(each_product))
    return Response(customized_product_list, status=200)


@api_view(['GET'])
def new_arrivals_api(request):
    new_arrivals_list = []
    new_arrivals_products = product.objects.all().order_by('-id')[:10]
    for each_product in new_arrivals_products:
        new_arrivals_list.append(makeObject(each_product))
    return Response(new_arrivals_list, status=200)


@api_view(['GET'])
def top_selling_api(request):
    top_selling_list = []
    top_selling_products = list(product.objects.all())
    random_top_selling_products = random.sample(top_selling_products, 10)
    for each_product in random_top_selling_products:
        top_selling_list.append(makeObject(each_product))
    return Response(top_selling_list, status=200)

# -------------------------------------------------------------------------------------------------------

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
