from django.contrib import admin
from .models import *


class readFields(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'modified_at', 'deleted_at')


admin.site.register(productCategory, readFields)
admin.site.register(productInventory, readFields)
admin.site.register(product, readFields)
admin.site.register(userDB)
admin.site.register(cart)
