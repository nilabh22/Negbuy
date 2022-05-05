from django.contrib import admin
from .models import *


class productFields(admin.ModelAdmin):
    list_display = ('name', 'brand')


class categoryFields(admin.ModelAdmin):
    list_display = ('name', 'id')


class cartFields(admin.ModelAdmin):
    list_display = ('order_number', 'order_price', 'order_status')


class portFields(admin.ModelAdmin):
    list_display = ('name', 'country')


class orderFields(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'status', 'order_date')


class bankFields(admin.ModelAdmin):
    list_display = ('accountName', 'accountNumber', 'accountIfsc')


class userFields(admin.ModelAdmin):
    list_display = ('seller_name', 'id', 'phone', 'role')


admin.site.register(productCategory, categoryFields)
admin.site.register(productInventory)
# admin.site.register(paymentTermFields, readIdField)
admin.site.register(product, productFields)
admin.site.register(productImages)
admin.site.register(userDB, userFields)
admin.site.register(cart, cartFields)
admin.site.register(bankDetail, bankFields)
admin.site.register(port, portFields)
admin.site.register(orders, orderFields)
admin.site.register(contact_data)
admin.site.register(primary_category)
