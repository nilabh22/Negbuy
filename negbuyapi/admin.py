from django.contrib import admin
from .models import *


class readIdField(admin.ModelAdmin):
    readonly_fields = ('id',)


class readFields(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'modified_at', 'deleted_at')


admin.site.register(productCategory, readFields)
admin.site.register(productInventory, readFields)
admin.site.register(paymentTermFields, readIdField)
admin.site.register(product, readFields)
admin.site.register(productImages)
admin.site.register(userDB, readIdField)
admin.site.register(cart)
admin.site.register(bankDetail)
admin.site.register(port)
admin.site.register(orders)
admin.site.register(contact_data)