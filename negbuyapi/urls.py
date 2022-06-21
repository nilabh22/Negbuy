from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('api/login', views.login, name="negbuy_login"),
    path('api/seller_login', views.seller_login, name="negbuy_seller_login"),
    path('api/seller_signup', views.seller_signup, name="negbuy_seller_signup"),

    path('api/product_info', views.product_info, name="product_info"),
    path('api/product_upload_api', views.product_upload_api,
         name="product_upload_api"),
    path('api/featured_product', views.featured_product_api,
         name="featured_product"),
    path('api/fast_dispatch', views.fast_dispatch_api, name="fast_dispatch"),
    path('api/ready_to_ship', views.ready_to_ship_api, name="ready_to_ship"),
    path('api/customized_product', views.customized_product_api,
         name="customized_product"),
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
    path('api/delete_product', views.delete_product, name="delete_product"),

    path('api/product_detail', views.product_detail, name="product_detail"),
    path('api/best_selling', views.best_selling, name="best_selling_product"),
    path('api/hot_selling', views.hot_selling, name="hot_selling_product"),
    path('api/categorized_product',
         views.categorized_product, name="product_category"),
    path('api/read_json', views.read_json, name="read_json"),
    path('api/add_ports', views.add_ports, name="add_ports"),

    path('api/my_orders', views.my_orders, name="my_orders"),
    path('api/order_history', views.order_history, name="order_history"),
<<<<<<< HEAD
    path('api/order_note', views.order_note, name="order_note"),
    path('api/order_details', views.order_details, name="order_details"),
    path('api/read_csv', views.read_csv, name="read_csv"),
    path('api/port_distance', views.port_distance, name="port_distance"),
    path('api/post_review', views.post_review, name="post_review"),
    path('api/product_reviews', views.product_reviews, name="product_reviews"),
    path('api/upload_product', views.upload_product, name="upload_product"),
    path('api/video_upload', views.video_upload, name="video_upload"),
    path('api/size_api', views.size_api),
    path('api/update_inventory', views.update_inventory, name="update_inventory"),
    path('api/get_inventory', views.get_inventory, name="get_inventory"),
    path('api/db_rfq', views.db_rfq),
    path('api/inventory_detail', views.inventory_detail, name="inventory_detail"),
=======

    path('api/read_csv', views.read_csv),
    path('api/rfq_db', views.api_RFQ),
    path('api/buyer_questions',views.api_buyer_questions),
    path('api/db_rfq', views.db_rfq),

    path('api/size_api', views.size_api),
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
