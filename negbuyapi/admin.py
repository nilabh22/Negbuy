from django.contrib import admin
from .models import *

# Register your models here.

class readOnlyId(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User_db, readOnlyId)
admin.site.register(Merchant_db, readOnlyId)
admin.site.register(Product_db, readOnlyId)