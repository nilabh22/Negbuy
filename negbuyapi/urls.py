from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
     path('api/login', views.login, name="negbuy_login"),
     path('api/seller_login', views.seller_login, name="negbuy_seller_login"),
     path('api/seller_signup', views.seller_signup, name="negbuy_seller_signup"),

     path('api/product_info', views.product_info, name="product_info"),
     path('api/product_upload_api', views.product_upload_api, name="product_upload_api"),
     path('api/featured_product', views.featured_product_api, name="featured_product"),
     path('api/fast_dispatch', views.fast_dispatch_api, name="fast_dispatch"),
     path('api/ready_to_ship', views.ready_to_ship_api, name="ready_to_ship"),
     path('api/customized_product', views.customized_product_api, name="customized_product"),
     path('api/new_arrivals', views.new_arrivals_api, name="new_arrivals"),
     path('api/top_selling', views.top_selling_api, name="top_selling"),
     path('api/user_products', views.user_products_api, name="user_products"),

     path('api/add_to_cart', views.add_to_cart, name="add_to_cart"),
     path('api/remove_from_cart', views.remove_from_cart, name="remove_from_cart"),
     path('api/my_cart', views.my_cart, name="my_cart"),

     path('api/verify_gst', views.verify_gst, name="verify_gst"),
     path('api/bank_details', views.bank_details, name="bank_details"),
     path('api/seller_details', views.seller_details, name="seller_details"),

     path('api/search_category', views.search_category, name="search_category"),
     path('api/get_ports', views.get_ports, name="get_ports"),
     path('api/get_categories', views.get_categories, name="get_categories"),

     path('api/get_orders', views.get_orders, name="get_orders"),

     path('api/contactus', views.contactus_function, name="contactus_function"),
     path('api/delete_product',views.delete_product, name="delete_product")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
