from django.contrib import admin
from .models import *


class readIdField(admin.ModelAdmin):
    readonly_fields = ('id',)


class readFields(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'modified_at', 'deleted_at')


class productFields(admin.ModelAdmin):
    list_display = ('id','name', 'brand')


class cartFields(admin.ModelAdmin):
    list_display = ('order_number', 'order_price', 'order_status')


class portFields(admin.ModelAdmin):
    list_display = ('name', 'country')


class orderFields(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'order_date')


class bankFields(admin.ModelAdmin):
    list_display = ('accountName', 'accountNumber', 'accountIfsc')


admin.site.register(productCategory, readFields)
admin.site.register(productInventory, readFields)
# admin.site.register(paymentTermFields, readIdField)
admin.site.register(product, productFields)
admin.site.register(productImages)
admin.site.register(userDB, readIdField)
admin.site.register(cart, cartFields)
admin.site.register(bankDetail, bankFields)
admin.site.register(port, portFields)
admin.site.register(orders, orderFields)
admin.site.register(contact_data)
admin.site.register(primary_category)
admin.site.register(rfq_db)
admin.site.register(buyer_questions)
admin.site.register(rfq)


