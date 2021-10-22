from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

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



