from django.contrib import admin
from .models import *


<<<<<<< HEAD
class productFields(admin.ModelAdmin):
    list_display = ('name', 'id', 'brand', 'user', 'category_id')


class imageFields(admin.ModelAdmin):
    list_display = ('product', 'id', 'image', 'main_image', 'color')


class categoryFields(admin.ModelAdmin):
    list_display = ('name', 'id')


class cartFields(admin.ModelAdmin):
    list_display = ('buyer_info', 'product', 'order_number',
                    'order_price', 'order_status')
=======
class readIdField(admin.ModelAdmin):
    readonly_fields = ('id',)


class readFields(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'modified_at', 'deleted_at')


class productFields(admin.ModelAdmin):
    list_display = ('id','name', 'brand')


class cartFields(admin.ModelAdmin):
    list_display = ('order_number', 'order_price', 'order_status')
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5


class portFields(admin.ModelAdmin):
    list_display = ('name', 'country')


class orderFields(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('product_info', 'order_number',
                    'status', 'user', 'order_date', 'id')


class bankFields(admin.ModelAdmin):
    list_display = ('accountName', 'accountNumber', 'accountIfsc', 'user')


class userFields(admin.ModelAdmin):
    list_display = ('seller_name', 'user_id', 'phone', 'role')


class reviewFields(admin.ModelAdmin):
    list_display = ('review_title', 'product', 'rating', 'user')


class productDetailFields(admin.ModelAdmin):
    list_display = ('product', 'id', 'heading',)


class contactFields(admin.ModelAdmin):
    list_display = ('message',)


class inventoryFields(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'color', 'size',)


class rfqFields(admin.ModelAdmin):
    list_display = ('requirement', 'quantity', 'target_price', 'date',)


admin.site.register(productCategory, categoryFields)
admin.site.register(product, productFields)
admin.site.register(productImages, imageFields)
admin.site.register(userDB, userFields)
=======
    list_display = ('order_number', 'status', 'order_date')


class bankFields(admin.ModelAdmin):
    list_display = ('accountName', 'accountNumber', 'accountIfsc')


admin.site.register(productCategory, readFields)
admin.site.register(productInventory, readFields)
# admin.site.register(paymentTermFields, readIdField)
admin.site.register(product, productFields)
admin.site.register(productImages)
admin.site.register(userDB, readIdField)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
admin.site.register(cart, cartFields)
admin.site.register(bankDetail, bankFields)
admin.site.register(port, portFields)
admin.site.register(orders, orderFields)
<<<<<<< HEAD
admin.site.register(contact_data, contactFields)
admin.site.register(primary_category)
admin.site.register(review_db, reviewFields)
admin.site.register(product_detail_db, productDetailFields)
admin.site.register(Inventory, inventoryFields)
admin.site.register(rfq, rfqFields)
=======
admin.site.register(contact_data)
admin.site.register(primary_category)
admin.site.register(rfq_db)
admin.site.register(buyer_questions)
admin.site.register(rfq)


>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
