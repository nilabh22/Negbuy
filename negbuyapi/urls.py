from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    #path('', views.homepageView, name="homepage"),

    path('api/login', views.login, name="negbuy_login"),
    path('api/featured_product', views.featured_product_api,
         name="featured_product"),
    path('api/fast_dispatch', views.fast_dispatch_api, name="fast_dispatch"),
    path('api/ready_to_ship', views.ready_to_ship_api, name="ready_to_ship"),
    path('api/customized_product', views.customized_product_api,
         name="customized_product"),
    path('api/new_arrivals', views.new_arrivals_api, name="new_arrivals"),
    path('api/top_selling', views.top_selling_api, name="top_selling"),
    path('api/add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('api/my_cart', views.my_cart, name="mycart"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
