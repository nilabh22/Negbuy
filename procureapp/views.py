from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['GET'])
def login(request):
    user_id = int(request.headers['user-id'])
    data_list = []
    try:
        usr = Procurement_User.objects.get(user_id=user_id)
        data = {
            'status': False,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'phone': usr.mobile,
            'language': '',
            'user_bio': 0
        }
        data_list.append(data)
    except Procurement_User.DoesNotExist:  # User does not exists
        data = {
            'status': False,
            'language': '',
            'first_name': '',
            'last_name': ''
        }
        data_list.append(data)
    finally:
        return Response(data_list, status=200)


@api_view(['GET'])
def signup(request):
    id = int(request.headers['user-id'])
    try:
        usr = Procurement_User.objects.get(user_id=id)
        data = {
            'status': True,
            'user_id': usr.user_id,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'phone': usr.mobile,
            'organization': usr.organization
        }
    except:
        data = {
            'status': False,
            'message': 'User Does Not Exists'
        }
    finally:
        return Response(data, status=200)


@api_view(['POST'])
def RFQ_generation(request):

    try:
        user_id = request.headers['User-id']
        LOGGED_user = Procurement_User.objects.get(user_id=user_id)
        Item_name = request.data.get('item_name')
        Category = request.data.get('category')
        Quantity = request.data.get('quantity')
        Model_Information = request.data.get('model_information')
        Delivery_Time_Duration = request.data.get('delivery_time_duration')
        Price_Range = request.data.get('price_range')
        RFQ_type = request.data.get('RFQ_type')

        try:
            RFQ_image = request.FILES['RFQ_image']
        except:
            RFQ_image = None

        if RFQ_type == 'SI':
            SI_Generated_RFQ = Generated_RFQ.objects.create(
                user=LOGGED_user,
                Item_name=Item_name,
                Category=Category,
                Quantity=Quantity,
                Model_Information=Model_Information,
                Delivery_Time_Duration=Delivery_Time_Duration,
                Price_Range=Price_Range,
                RFQ_type=RFQ_type,
                RFQ_image=RFQ_image
            )
            SI_Generated_RFQ.save()

        else:
            SI_Generated_RFQ = Generated_RFQ.objects.create(
                user=LOGGED_user,
                Category=Category,
                RFQ_type=RFQ_type,
                RFQ_image=RFQ_image
            )
            SI_Generated_RFQ.save()

        return Response('Success', status=200)
    except:
        return Response('Error', status=200)


@api_view(['POST'])
def Dashboard_api_function(request):
    
    user_id = request.headers['User-id']
    User_RFQ_data = Generated_RFQ.objects.filter(user=user_id)
    User_RFQ_list=list()
    for data in User_RFQ_data:
        if data.RFQ_type == 'SI':
            qwe = {
                'Product_name':data.Item_name,
                'RFQ_type':data.RFQ_type,
                'Status':data.RFQ_status,
                'RFQ_image':data.RFQ_image.url,
            }
        else:
            qwe = {
                'Product_name':data.RFQ_type,
                'Status':data.RFQ_status,
                'RFQ_image':data.RFQ_image.url,
            }
        User_RFQ_list.append(qwe)
    
    return Response(User_RFQ_list, status=200)