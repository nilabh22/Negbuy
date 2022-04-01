from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from drf_api_logger import API_LOGGER_SIGNAL
from .models import *
import random
import requests
import bs4
import datetime
import os
from .contactus import contact_function

@api_view(['POST'])
def login(request):
    user_id = request.headers['User-id']
    phone = request.data['phone']

    try:
        usr = userDB.objects.get(user_id=user_id)
        response = {
            'status': False,
            'user_id': usr.user_id,
            'phone': usr.phone,
            'first_name': usr.first_name,
            'last_name': usr.last_name,
            'language': '',
            'user_bio': 0 if usr.first_name == None else 1,
        }

    except:
        userDB.objects.create(
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
def seller_login(request):
    phone = request.data['phone']
    password = request.data['password']

    try:
        usr = userDB.objects.get(role='Seller', phone=phone, password=password)
        try:
            usrBank = bankDetail.objects.get(user=usr)
            accountName = usrBank.accountName
            accountNumber = usrBank.accountNumber
            accountIfsc = usrBank.accountIfsc
        except:
            accountName = None
            accountNumber = None
            accountIfsc = None
        response = {
            'status': True,
            'user_id': usr.user_id,
            'phone': usr.phone,
            'password': usr.password,
            'seller_name': usr.seller_name,
            'date_of_birth': usr.date_of_birth,
            'company': usr.company,
            'gst_number': usr.gst_number,
            'account_name': accountName,
            'account_number': accountNumber,
            'account_ifsc': accountIfsc
        }

    except Exception as e:
        response = {
            'status': False,
            'message': 'Incorrect phone or password',
            'error_msg': str(e)
        }

    finally:
        return Response(response, status=200)


@api_view(['POST'])
def seller_signup(request):
    user_id = request.headers['User-id']
    password = request.data['password']
    phone = request.data['phone']

    try:
        usr = userDB.objects.get(Q(user_id=user_id) | Q(phone=phone))
        sameField = 'User Id ' if usr.user_id == user_id else 'Phone number '
        response = {
            'status': False,
            'message': sameField + 'already exists'
        }

    except:
        userDB.objects.create(
            user_id=user_id,
            password=password,
            phone=phone,
            role="Seller"  
        )
        response = {
            'status': True,
            'user_id': user_id,
            'phone': phone,
            'password': password,
            'seller_name':'',
        }

    finally:
        return Response(response, status=200)


def addProduct(request, user):
    price_choice = request.data['price_choice'].lower()

    category = request.data['category']
    try:
        category_record = productCategory.objects.get(name=category)
    except:
        category_record = productCategory.objects.create(name=category)

    if price_choice == 'add price':
        product_record = product.objects.create(
            user = user,
            name = request.data['name'],
            category_id = category_record,
            brand = request.data['brand'],
            keyword = request.data['keywords'],
            color = request.data['colors'],
            size = request.data['size'],
            details = request.data['details'],
            price_choice = price_choice,
            price = request.data['price'],
            mrp =  request.data['mrp'],
            sale_price = request.data['sale_price'],
            sale_startdate = request.data['sale_startdate'],
            sale_enddate = request.data['sale_enddate'],
            manufacturing_time = request.data['manufacturing_time'],
            maximum_order_quantity = request.data['maximum_order_quantity'],
            #terms = terms_record,
            weight = request.data['weight'],
            transportation_port = request.data['transportation_port'],
            packing_details = request.data['packing_details'],
            packing_address =  request.data['packing_address']
        )
        product_record.save()
        images = dict((request.data).lists())['image']
        for image in images:
            productImages.objects.create(product = product_record, image = image)

    elif price_choice == 'price according to quantity':
        product_record = product.objects.create(
            user = user,
            name = request.data['name'],
            category_id = category_record,
            keyword = request.data['keywords'],
            color = request.data['colors'],
            size = request.data['size'],
            details = request.data['details'],
            price_choice = price_choice,
            quantity_price = request.data['quantity_price'],
            #terms = terms_record,
            weight = request.data['weight'],
            transportation_port = request.data['transportation_port'],
            packing_details = request.data['packing_details'],
            packing_address =  request.data['packing_address']
        )
        product_record.save()
        images = dict((request.data).lists())['image']
        for image in images:
            productImages.objects.create(product = product_record, image = image)


@api_view(['POST'])
def product_upload_api(request):
    user_id = request.headers['User-id']
    try:
        user = userDB.objects.get(user_id=user_id, role='Seller')
        addProduct(request, user)
        return Response({'success': 'Product Added'}, status=200)
    except Exception as e:
        return Response({'status': 'Error', 'error_msg': str(e)})


def getProductObject(product):
    try:
        inventory = product.inventory_id.quantity
    except:
        inventory = ''

    try:
        prodImages = productImages.objects.filter(product=product)
        imageURL = []
        for prodImage in prodImages:
            imageURL.append(prodImage.image.url)
    except:
        imageURL = []

    detailsList = []
    list = [str.strip() for str in product.details.split(',')]
    for eachDetail in list:
        keyValue = eachDetail.split(':')
        detailsObject = {
            'title': keyValue[0].strip(),
            'description': keyValue[1].strip(),
        }
        detailsList.append(detailsObject)

    object = {
        'id': product.id,
        'name': product.name,
        'sku': product.sku,
        'category': product.category_id.name,
        'inventory': inventory,
        'image': imageURL,
        'featured_products': product.featured_products,
        'fast_dispatch': product.fast_dispatch,
        'ready_to_ship': product.ready_to_ship,
        'customized_product': product.customized_product,
        'brand':product.brand,
        'keyword': [str.strip() for str in product.keyword.split(',')],
        'color':[str.strip() for str in product.color.split(',')],
        'size': [str.strip() for str in product.size.split(',')],
        'details': detailsList,
        'price_choice': product.price_choice,
        'price': product.price,
        'mrp': product.mrp,
        'sale_price': product.sale_price,
        'sale_startdate': product.sale_startdate,
        'sale_enddate': product.sale_enddate,
        'manufacturing_time': product.manufacturing_time,
        'quantity_price': product.quantity_price,
        'maximum_order_quantity': product.maximum_order_quantity,
        'weight': product.weight,
        'transportation_port': product.transportation_port,
        'packing_details': product.packing_details,
        'packing_address': product.packing_address,
        'status': product.status,
        'created_at': product.created_at,
        'modified_at': product.modified_at,
        'deleted_at': product.deleted_at,
        'rating': {
            'rate': 3.0,
            'count': 430
        }
    }
    return object


@api_view(['POST'])
def product_info(request):
    try:
        product_id = request.data['product_id']
        product_info = product.objects.get(id=product_id)
        product_object = getProductObject(product_info)
        return Response(product_object, status=200)
    except Exception as e:
        return Response({'status': 'Product id does not exists', 'error_msg': str(e)})


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

    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)}, status=401)


@api_view(['POST'])
def remove_from_cart(request):
    user_id = request.headers['User-id']

    try:
        usr = userDB.objects.get(user_id=user_id)
        product_id = int(request.data['product_id'])
        removed_quantity = int(request.data['removed_quantity'])
        item_quantity = cart.objects.get(user_id=usr.id, product_id=product_id).quantity
        new_quantity = item_quantity - removed_quantity

        if new_quantity <= 0:
            cart.objects.get(user_id=usr.id, product_id=product_id).delete()
            return Response({'status': 'success', 'msg': 'item removed from cart'})
        else:
            record = cart.objects.get(user_id=usr.id, product_id=product_id)
            record.quantity = new_quantity
            record.save()
            return Response({'status': 'success', 'msg': 'item quantity decreased to ' + str(new_quantity)})

    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)})


@api_view(['GET'])
def my_cart(request):
    status = 200
    cart_items = []
    user_id = request.headers['User-id']
    try:
        usr = userDB.objects.get(user_id=user_id)
        all_items = cart.objects.filter(user_id=usr.id)
        for each_item in all_items:
            object = getProductObject(each_item.product)
            object['quantity'] = each_item.quantity
            cart_items.append(object)
    except:
        status = 401

    return Response(cart_items, status=status)


@api_view(['GET'])
def user_products_api(request):
    user_id = request.headers['User-id']
    response = []
    try:
        user = userDB.objects.get(user_id=user_id, role='Seller')
        user_products = product.objects.filter(user=user)
        for each_product in user_products:
            response.append(getProductObject(each_product))
    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)}, status=401)

    return Response(response, status=200)


def getGstObject(gst_number, divData):
    object = {
        'gst_number': gst_number,
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
    user_id = request.headers['User-id']
    gst_number = request.data['gstNo']

    try:
        usr = userDB.objects.get(user_id=user_id, role='Seller')
        addr = "https://irisgst.com/gstin-filing-detail/?gstinno=" + gst_number
        response = requests.get(addr)
        htmlPage = bs4.BeautifulSoup(response.text, "html.parser")
        divData = htmlPage.find_all('div', {'class':'form-group'})
        response = getGstObject(gst_number, divData)
        usr.gst_number = gst_number
        usr.save(update_fields=['gst_number'])
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


@api_view(['POST'])
def seller_details(request):
    user_id = request.headers['User-id']

    try:
        usr = userDB.objects.get(user_id=user_id, role='Seller')
        usr.seller_name = request.data['seller_name']
        usr.date_of_birth = request.data['date_of_birth']
        usr.email = request.data['email']
        usr.company = request.data['company']
        usr.address = request.data['address']
        usr.document_verification = request.FILES['document_verification']
        usr.save(update_fields=['seller_name', 'date_of_birth', 'email', 'company', 'address', 'document_verification'])
        return Response({'status': 'success'}, status=200)

    except Exception as e:
        return Response({'status': 'error', 'error_msg': str(e)}, status=401)


@api_view(['POST'])
def search_category(request):
    response = []
    category_selected = request.data['category_selected']
    raw_string = request.data['category']
    keywords = raw_string.replace('>', '').replace('& ', '').replace('and ', '').strip()
    print(category_selected, raw_string, keywords)

    if len(keywords) == 0:
        return Response(response, status=200)
    else:
        file_path = 'static/categories/'+str(category_selected).strip()+'.txt'
        print(file_path)
        with open(file_path) as file:
            for line in file:
                if keywords.lower() in line.lower().replace('& ', ''):
                    response.append(line.strip())
            if len(response) == 0:
                keywords = keywords.replace(',', '')
                keywordList = keywords.split(' ')
                with open(file_path) as file:
                    for line in file:
                        if any(keyword.lower() in line.lower() for keyword in keywordList):
                            response.append(line.strip())
        return Response(response, status=200)


def getPort(port):
    name = port.name
    state = port.state
    return name + ',' + state


@api_view(['GET'])
def get_ports(request):
    response = []
    all_ports = port.objects.all()
    for each_port in all_ports:
        response.append(getPort(each_port))
    return Response(response, status=200)

@api_view(['GET'])
def get_categories(request):
    try:
        #/home/vf2586e813kg/api.negbuy/static
        path = "/home/vf2586e813kg/api.negbuy/static/categories"
        dir_list = os.listdir(path)
        mylst = map(lambda each:each.strip(".txt"), dir_list)

        return Response({
            'status':True,
            'message':'Success',
            'data':mylst
        })
    except Exception as e:
        return Response({
            'status':False,
            'message':e,
            'data':''
        })
    
@api_view(['GET'])
def get_orders(request):
    user_id = request.headers['User-id']
    all_orders_list = list()
    try:
        usr = userDB.objects.get(user_id=user_id, role='Seller')
        #get orders details
        all_orders = orders.objects.filter(user=usr)
        for each_order in all_orders:
            obj = {
                'order_date':each_order.created_at,
                'order_number':each_order.order_number,
                'product_name':each_order.product_info.name,
                'product_quantity':each_order.order_quantity,
                'ship_date':each_order.shipping_date,
                'delivery_date':each_order.delivery_date,
                'order_status':each_order.status
            }

            all_orders_list.append(obj)
        return Response({
            'status':True,
            'message':'Success',
            'data':all_orders_list
        })
    except Exception as e:
        return Response({
            'status':False,
            'message':e,
            'data':''
        })


@api_view(['POST'])
def contactus_function(request):
    try:
        name = request.data['name']
        contact_num = request.data['number']
        req_email = request.data['email']
        message = request.data['message']
        full_message = "Please contact "+name+" "+contact_num+" "+req_email+" for "+message
        cont_res = contact_data.objects.create(message=full_message)
        if cont_res:
            return Response({
                    'status':True,
                    'message':'Success',
                    'data':"Message sent"
                })
        else:
            return Response({
                    'status':False,
                    'message':'Error',
                    'data':"Please enter details again"
                })
    except:
        return Response({
                    'status':False,
                    'message':'Error',
                    'data':"Please enter details again"
                })

@api_view(['POST'])
def delete_product(request):
    try:
        user = request.headers['User-id']
        product_id = request.data['product_id']

        user_details = userDB.objects.get(user_id = user)
        product_details = product.objects.get(id=product_id, user=user_details).delete()
  
        
        return Response({
                    'status':True,
                    'message':'Success',
                    'data':"Deleted successfully"
                })
    except Exception as e:
        return Response({
                'status':False,
                'message':'Error',
                'data':str(e)
            })
    