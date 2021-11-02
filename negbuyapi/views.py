from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import random

# Create your views here.

@api_view(['GET'])
def product_list(request):
    #in future will be changed according to user 
    #for now testing version
    all_products = Product_db.objects.all()

    product_list_ = list()
    for each_product in all_products:
        each_obj = {
            'id':each_product.id,
            'title':each_product.title,
            'price':each_product.price,
            'description':each_product.description,
            'category':None,
            'image':each_product.image.url,
            'rating':{
                'rate':3.0,
                'count':430
            }
        }

        product_list_.append(each_obj)

    return Response(product_list_, status=200)


@api_view(['GET'])
def mostvalued_fastdispatch(request):

    #in future will be changed according to user 
    #for now testing version
    all_products = list(Product_db.objects.all())

    Most_valued_product = random.sample(all_products, 4)
    most_valued = list()
    fast_dispatch = list()

    for i in Most_valued_product:
        qwe = {
            'id':i.id,
            'title':i.title,
            'price':i.price,
            'description':i.description,
            'category':None,
            'image':i.image.url,
            'rating':{
                'rate':3.0,
                'count':430
            }
        }

        most_valued.append(qwe)
    
    for i in all_products:
        if len(fast_dispatch) < 4:
            if i.fast_dispatch == 'True':
                qwe = {
                    'id':i.id,
                    'title':i.title,
                    'price':i.price,
                    'description':i.description,
                    'category':None,
                    'image':i.image.url,
                    'rating':{
                        'rate':3.0,
                        'count':430
                    }
                }

                fast_dispatch.append(qwe)
        else:
            break


    return Response({'Most_valued':most_valued, 'fast_dispatch':fast_dispatch}, status=200)



