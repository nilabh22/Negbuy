from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['GET'])
def login(request):
    user_id = request.headers['User-id']
    phone = request.data['phone']
    data_list = list()

    try:
        usr = Procurement_User.objects.get(user_id=user_id)
        data = {
            'status': False,
            'phone': usr.phone,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'language': '',
            'user_bio': 0 if usr.first_name == None else 1,
        }
        data_list.append(data)

    except:
        new_user_data = Procurement_User.objects.create(
            user_id=user_id, phone=phone)
        new_user_data.save()
        data = {
            'status': True,
            'phone': phone,
            'first_name': '',
            'last_name': '',
        }
        data_list.append(data)

    finally:
        return Response(data_list, status=200)


@api_view(['POST'])
def signup(request):
    user_id = request.headers['User-id']
    data_list = list()

    try:
        usr = Procurement_User.objects.get(user_id=user_id)
        usr.first_name = request.data['first_name']
        usr.last_name = request.data['last_name']
        usr.organization = request.data['organization']
        usr.save(update_fields=['first_name', 'last_name', 'organization'])

        data = {
            'status': True,
            'user_id': usr.user_id,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'phone': usr.phone,
            'organization': usr.organization
        }
        data_list.append(data)

    except:
        data = {
            'status': False,
            'message': 'User Does Not Exists'
        }
        data_list.append(data)

    finally:
        return Response(data_list, status=200)


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
    User_RFQ_data = Generated_RFQ.objects.filter(user__user_id=user_id)
    User_RFQ_list = list()
    for data in User_RFQ_data:
        if data.RFQ_type == 'SI':
            qwe = {
                'Product_name': data.Item_name,
                'RFQ_type': data.RFQ_type,
                'Status': data.RFQ_status,
                'RFQ_image': data.RFQ_image.url,
            }
        else:
            qwe = {
                'Product_name': data.RFQ_type,
                'Status': data.RFQ_status,
                'RFQ_image': data.RFQ_image.url,
            }
        User_RFQ_list.append(qwe)

    return Response(User_RFQ_list, status=200)
