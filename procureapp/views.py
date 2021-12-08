from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import datetime


@api_view(['POST'])
def login(request):
    user_id = request.headers['User-id']
    phone = request.data['phone']

    try:
        usr = procurementUser.objects.get(user_id=user_id)
        response = {
            'status': False,
            'user_id': user_id,
            'phone': usr.phone,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'language': '',
            'user_bio': 0 if usr.first_name == None else 1,
        }

    except:
        procurementUser.objects.create(
            user_id=user_id,
            phone=phone
        )
        response = {
            'status': True,
            'user_id': user_id,
            'phone': phone,
            'first_name': '',
            'last_name': '',
        }

    finally:
        return Response(response, status=200)


@api_view(['POST'])
def signup(request):
    user_id = request.headers['User-id']

    try:
        usr = procurementUser.objects.get(user_id=user_id)
        usr.first_name = request.data['first_name']
        usr.last_name = request.data['last_name']
        usr.email = request.data['email']
        usr.organization = request.data['organization']
        usr.save(update_fields=['first_name',
                 'last_name', 'email', 'organization'])

        response = {
            'status': True,
            'user_id': usr.user_id,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'phone': usr.phone,
            'email': usr.email,
            'organization': usr.organization
        }

    except:
        response = {
            'status': False,
            'message': 'User Does Not Exists'
        }

    finally:
        return Response(response, status=200)


@api_view(['POST'])
def RFQ_generation(request):

    try:
        user_id = request.headers['User-id']
        user = procurementUser.objects.get(user_id=user_id)
        rfq_type = request.data['RFQ_type']
        category = request.data['category']
        try:
            rfq_image = request.FILES['RFQ_image']
        except:
            rfq_image = None

        if rfq_type == 'SI':
            item_name = request.data['item_name']
            quantity = request.data['quantity']
            model_information = request.data['model_information']
            delivery_time_duration = request.data['delivery_time_duration']
            price_range = request.data['price_range']

            generatedRFQ.objects.create(
                user=user,
                item_name=item_name,
                category=category,
                quantity=quantity,
                model_information=model_information,
                delivery_time_duration=delivery_time_duration,
                price_range=price_range,
                rfq_type=rfq_type,
                rfq_image=rfq_image,
                datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

        else:
            generatedRFQ.objects.create(
                user=user,
                category=category,
                rfq_type=rfq_type,
                rfq_image=rfq_image,
                datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

        return Response({'status': 'success'}, status=200)
    except:
        return Response({'status': 'error'}, status=200)


@api_view(['GET'])
def Dashboard_api_function(request):

    user_id = request.headers['User-id']
    User_RFQ_data = generatedRFQ.objects.filter(user__user_id=user_id)
    User_RFQ_list = list()

    for data in User_RFQ_data:
        try:
            rfq_image = data.rfq_image.url
        except:
            rfq_image = ''

        if data.rfq_type == 'SI':
            qwe = {
                'rfq_name': data.category + " " + data.datetime,
                'rfq_type': data.rfq_type,
                'status': data.rfq_status,
                'product_name': data.item_name,
                'rfq_image': rfq_image,
                'category': data.category,
                'datetime': data.datetime
            }
        else:
            qwe = {
                'rfq_name': data.category + " " + data.datetime,
                'rfq_type': data.rfq_type,
                'status': data.rfq_status,
                'rfq_image': rfq_image,
                'category': data.category,
                'datetime': data.datetime
            }
        User_RFQ_list.append(qwe)

    return Response(User_RFQ_list, status=200)
