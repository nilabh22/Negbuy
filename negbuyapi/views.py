from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import random
import requests
import bs4



def getOldLoginObject(usr, isSeller=False):
    if isSeller:
        object = {
            'status': False,
            'user_id': usr.user_id,
            'phone': usr.phone,
            'password': usr.password,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'language': '',
            'user_bio': 0 if usr.first_name == None else 1,
        }
    else:
        object = {
            'status': False,
            'user_id': usr.user_id,
            'phone': usr.phone,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'language': '',
            'user_bio': 0 if usr.first_name == None else 1,
        }
    return object  


def getNewLoginObject(user_id, phone, password='', isSeller=False):
    if isSeller:
        object = {
            'status': True,
            'user_id': user_id,
            'phone': phone,
            'password': password,
            'first_name': '',
            'last_name': '',
        }
    else:
        object = {
            'status': True,
            'user_id': user_id,
            'phone': phone,
            'first_name': '',
            'last_name': '',
        }
    return object


@api_view(['POST'])
def login(request):
    user_id = request.headers['User-id']
    phone = request.data['phone']

    try:
        usr = userDB.objects.get(user_id=user_id)
        response = getOldLoginObject(usr)

    except:
        userDB.objects.create(
            user_id=user_id,
            phone=phone
        )
        response = getNewLoginObject(user_id, phone)

    finally:
        return Response(response, status=200)


@api_view(['POST'])
def seller_login(request):
    user_id = request.headers['User-id']
    password = request.data['password']
    phone = request.data['phone']

    try:
        usr = userDB.objects.get(user_id=user_id)
        response = getOldLoginObject(usr, True)

    except:
        userDB.objects.create(
            user_id=user_id,
            password=password,
            phone=phone,
            role="Seller"  
        )
        response = getNewLoginObject(user_id, phone, password, True)

    finally:
        return Response(response, status=200)


def getProductObject(product):
    try:
        imageURL = product.image.url
    except:
        imageURL = ''
    object = {
        'id': product.id,
        'name': product.name,
        'description': product.desc,
        'price': product.price,
        'category': product.category_id.name,
        'image': imageURL,
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
        featured_product_list.append(getProductObject(each_product))

    if len(featured_product_list) != 10:
        products = list(product.objects.filter(featured_products=False))
        random_products = random.sample(
            products, 10-len(featured_product_list))
        for each_product in random_products:
            featured_product_list.append(getProductObject(each_product))

    return Response(featured_product_list, status=200)


@api_view(['GET'])
def fast_dispatch_api(request):
    fast_dispatch_list = []
    fast_dispatch_products = product.objects.filter(fast_dispatch=True)[:10]
    for each_product in fast_dispatch_products:
        fast_dispatch_list.append(getProductObject(each_product))

    if len(fast_dispatch_list) != 10:
        products = list(product.objects.filter(fast_dispatch=False))
        random_products = random.sample(
            products, 10-len(fast_dispatch_list))
        for each_product in random_products:
            fast_dispatch_list.append(getProductObject(each_product))
    return Response(fast_dispatch_list, status=200)


@api_view(['GET'])
def ready_to_ship_api(request):
    ready_to_ship_list = []
    ready_to_ship_products = product.objects.filter(ready_to_ship=True)[:10]
    for each_product in ready_to_ship_products:
        ready_to_ship_list.append(getProductObject(each_product))

    if len(ready_to_ship_list) != 10:
        products = list(product.objects.filter(ready_to_ship=False))
        random_products = random.sample(
            products, 10-len(ready_to_ship_list))
        for each_product in random_products:
            ready_to_ship_list.append(getProductObject(each_product))
    return Response(ready_to_ship_list, status=200)


@api_view(['GET'])
def customized_product_api(request):
    customized_product_list = []
    customized_products = product.objects.filter(customized_product=True)[:10]
    for each_product in customized_products:
        customized_product_list.append(getProductObject(each_product))

    if len(customized_product_list) != 10:
        products = list(product.objects.filter(customized_product=False))
        random_products = random.sample(
            products, 10-len(customized_product_list))
        for each_product in random_products:
            customized_product_list.append(getProductObject(each_product))
    return Response(customized_product_list, status=200)


@api_view(['GET'])
def new_arrivals_api(request):
    new_arrivals_list = []
    new_arrivals_products = product.objects.all().order_by('-id')[:10]
    for each_product in new_arrivals_products:
        new_arrivals_list.append(getProductObject(each_product))
    return Response(new_arrivals_list, status=200)


@api_view(['GET'])
def top_selling_api(request):
    top_selling_list = []
    top_selling_products = list(product.objects.all())
    random_top_selling_products = random.sample(top_selling_products, 10)
    for each_product in random_top_selling_products:
        top_selling_list.append(getProductObject(each_product))
    return Response(top_selling_list, status=200)


@api_view(['POST'])
def add_to_cart(request):
    user_id = request.headers['User-id']

    try:
        usr = userDB.objects.get(user_id=user_id)
        product_id = int(request.data['product_id'])
        quantity = int(request.data['quantity'])

        try:
            record = cart.objects.get(user_id=usr.id, product_id=product_id)
            record.quantity = quantity
            record.save()
        except:
            cart.objects.create(
                user_id=usr.id,
                product_id=product_id,
                quantity=quantity,
            )
        return Response({'status': 'success'}, status=200)

    except:
        return Response({'status': 'error'}, status=401)


def getCartObject(item):
    object = {
        'name': item.product.name,
        'description': item.product.desc,
        'price': item.product.price,
        'category': item.product.category_id.name,
        'image': item.product.image.url,
        'quantity': item.quantity,
        'rating': {
            'rate': 3.0,
            'count': 430
        }
    }
    return object


@api_view(['GET'])
def my_cart(request):
    status = 200
    cart_items = []
    user_id = request.headers['User-id']

    try:
        usr = userDB.objects.get(user_id=user_id)
        all_items = cart.objects.filter(user_id=usr.id)
        for each_item in all_items:
            cart_items.append(getCartObject(each_item))

    except Exception as e:
        status = 401

    return Response(cart_items, status=status)


def getGstObject(divData):
    object = {
        'tradeName': divData[0].input.get('value'),
        'legalName': divData[1].input.get('value'),
        'type': divData[2].input.get('value'),
        'regDate': divData[3].input.get('value'),
        'constBusiness': divData[4].input.get('value'),
        'businessNature': divData[5].input.get('value'),
        'principalPlace': divData[6].input.get('value'),
    }
    return object


@api_view(['POST'])
def verify_gst(request):
    gstNo = request.data['gstNo']

    try:
        addr = "https://irisgst.com/gstin-filing-detail/?gstinno=" + gstNo
        response = requests.get(addr)
        htmlPage = bs4.BeautifulSoup(response.text, "html.parser")
        divData = htmlPage.find_all('div', {'class':'form-group'})
        response = getGstObject(divData)
        return Response(response, status=200)

    except:
        return Response({'status': 'Invalid GST Number'}, status=403)


@api_view(['POST'])
def bank_details(request):
    user_id = request.headers['User-id']

    try:
        usr = userDB.objects.get(user_id=user_id, role='Seller')
        accName = request.data['accName']
        accNo = request.data['accNo']
        ifsc = request.data['ifsc']

        bankDetail.objects.create(
            user_id=usr.id,
            accountName=accName,
            accountNumber=accNo,
            accountIfsc=ifsc
        )
        return Response({'status': 'success'}, status=200)

    except:
        return Response({'status': 'User does not exist'}, status=401)


def setSellerDetails(request, usr, aadhaar=None, pan=None):
    usr.first_name = request.data['first_name']
    usr.last_name = request.data['last_name']
    usr.date_of_birth = request.data['date_of_birth']
    usr.email = request.data['email']
    usr.company = request.data['company']
    usr.address = request.data['address']
    usr.aadhaar = aadhaar
    usr.pan = pan
    usr.save(update_fields=['first_name', 'last_name', 'email', 'company', 'address', 'aadhaar', 'pan'])


@api_view(['POST'])
def seller_details(request):
    user_id = request.headers['User-id']

    try:
        usr = userDB.objects.get(user_id=user_id, role='Seller')
        try:
            aadhaar = request.FILES['aadhaar']
            pan = request.FILES['pan']
            setSellerDetails(request, usr, aadhaar=aadhaar, pan=pan)
        except:
            try:
                aadhaar = request.FILES['aadhaar']
                setSellerDetails(request, usr, aadhaar=aadhaar)
            except:
                pan = request.FILES['pan']
                setSellerDetails(request, usr, pan=pan)
        return Response({'status': 'success'}, status=200)

    except:
        return Response({'status': 'User does not exist'}, status=401)
