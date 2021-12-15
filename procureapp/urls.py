from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login, name='procure_login'),
    path('signup', views.signup, name='procure_signup'),
    path('generate_RFQ', views.RFQ_generation, name='RFQ_generation'),
    path('dashboard', views.Dashboard_api_function,
         name='Dashboard_api_function'),
    path('categories', views.categories, name="categories"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
