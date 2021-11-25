from django.contrib import admin
from .models import *


class readFields(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'modified_at', 'deleted_at')


admin.site.register(product_category, readFields)
admin.site.register(product_inventory, readFields)
admin.site.register(product, readFields)
admin.site.register(order)
admin.site.register(userdb)


# class readOnlyId(admin.ModelAdmin):
#     readonly_fields = ('id',)

# admin.site.register(User_db, readOnlyId)
# admin.site.register(Merchant_db, readOnlyId)
# admin.site.register(Product_db, readOnlyId)
