from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['GET'])
def login(request):
    user_id = int(request.headers['user-id'])
    data_list = []
    try:
        usr = procure_userdb.objects.get(user_id=user_id)
        data = {
            'status': False,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'phone': usr.mobile,
            'language': '',
            'user_bio': 0
        }
        data_list.append(data)
    except procure_userdb.DoesNotExist:  # User does not exists
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
        usr = procure_userdb.objects.get(user_id=id)
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
