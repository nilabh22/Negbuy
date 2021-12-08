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

    user_id = models.CharField(max_length=1000, null=True, blank=True)
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
    phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name_plural = "User"
