from django.db import models


class product_category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class product_inventory(models.Model):
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Inventory: " + str(self.id) + " - Capacity: " + str(self.quantity)

    class Meta:
        verbose_name_plural = "Inventory"


class product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    sku = models.CharField(max_length=50)
    category_id = models.ForeignKey(product_category, on_delete=models.CASCADE)
    inventory_id = models.OneToOneField(
        product_inventory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    featured_products = models.BooleanField(default=False)
    fast_dispatch = models.BooleanField(default=False)
    ready_to_ship = models.BooleanField(default=False)
    customized_product = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"


class userdb(models.Model):

    user_roles = (
        ('Merchant', 'Merchant'),
        ('Buyer', 'Buyer'),
    )

    # user_id = models.CharField(max_length=1000, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    password = models.TextField(null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, choices=user_roles, default='Buyer')
    telephone = models.PositiveIntegerField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)
    address_line1 = models.CharField(max_length=50, null=True)
    address_line2 = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "User DB"


# ------------------------------------------------------------------------------------------------------
# Old Models

# class User_db(models.Model):

#     User_gender = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('other', 'other'),
#     )

#     language_choices = (
#         ('English', 'English'),
#         ('Hindi', 'Hindi'),
#     )

#     user_id = models.CharField(max_length=100, unique=True , null=True, blank=True)
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     Phone = models.CharField(max_length=50,unique=True, null=True, blank=True)
#     email = models.CharField(max_length=100,unique=True, null=True, blank=True)
#     gender = models.CharField(max_length=100, choices=User_gender, null=True, blank=True)
#     language = models.CharField(max_length=100,choices=language_choices, default='English', null=True, blank=True)
#     location = models.CharField(max_length=1000, null=True, blank=True)
#     state = models.CharField(max_length=100, null=True, blank=True)
#     country = models.CharField(max_length=100, null=True, blank=True)
#     district = models.CharField(max_length=100, null=True, blank=True)
#     pincode = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return self.user_id
#     class Meta:
#         verbose_name_plural = "User db"

# class Merchant_db(models.Model):

#     User_gender = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('other', 'other'),
#     )

#     language_choices = (
#         ('English', 'English'),
#         ('Hindi', 'Hindi'),
#     )

#     user_id = models.CharField(max_length=100, unique=True , null=True, blank=True)
#     first_name = models.CharField(max_length=100, null=True, blank=True)
#     last_name = models.CharField(max_length=100, null=True, blank=True)
#     Phone = models.CharField(max_length=50,unique=True, null=True, blank=True)
#     email = models.CharField(max_length=100,unique=True, null=True, blank=True)
#     gender = models.CharField(max_length=100,choices=User_gender, null=True, blank=True)
#     language = models.CharField(max_length=100, choices=language_choices, default='English', null=True, blank=True)
#     location = models.CharField(max_length=1000, null=True, blank=True)
#     state = models.CharField(max_length=100, null=True, blank=True)
#     country = models.CharField(max_length=100, null=True, blank=True)
#     district = models.CharField(max_length=100, null=True, blank=True)
#     pincode = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return self.user_id
#     class Meta:
#         verbose_name_plural = "Merchant db"

# class Product_db(models.Model):

#     fast_dispatch_choices = (
#         ('True','True'),
#         ('False','False')
#     )

#     user_id = models.ForeignKey(Merchant_db, on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=100, null=True, blank=True)
#     price = models.IntegerField(null=True, blank=True)
#     description = models.CharField(max_length=2000, null=True, blank=True)
#     category = models.CharField(max_length=2000, null=True, blank=True)  #in future a choice field
#     image = models.ImageField(upload_to='Product_images', default=None, blank=True)
#     fast_dispatch = models.CharField(max_length=100, choices=fast_dispatch_choices, null=True, blank=True)

#     def __str__(self):
#         return self.title
#     class Meta:
#         verbose_name_plural = "Product db"
