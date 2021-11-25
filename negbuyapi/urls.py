from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    #path('', views.homepageView, name="homepage"),
    # path('api/product_list', views.product_list, name="product_list"),
    # path('api/mostvalues_fastdispatch', views.mostvalued_fastdispatch, name="mostvalued_fastdispatch"),
    path('api/login', views.login, name="login"),
    path('api/featured_product', views.featured_product, name="featured_product"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
