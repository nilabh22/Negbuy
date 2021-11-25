from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

# Create your views here.


@api_view(['GET'])
def login(request):
    id = int(request.headers['Authorization'])
    data_list = []

    try:
        usr = procure_userdb.objects.get(id=id)
        data = {
            'status': "FALSE",
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'phone': usr.mobile,
            'language': '',
            'user_bio': ''
        }
        data_list.append(data)

    except procure_userdb.DoesNotExist:
        data = {
            'status': "FALSE",
            'language': '',
        }
        data_list.append(data)

    finally:
        return Response(data_list, status=200)
