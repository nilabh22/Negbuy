from django.db import models


class productCategory(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class productInventory(models.Model):
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
    category_id = models.ForeignKey(productCategory, on_delete=models.CASCADE)
    inventory_id = models.OneToOneField(productInventory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    image = models.ImageField(upload_to='Product_images', default=None, blank=True)
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


class userDB(models.Model):

    user_roles = (
        ('Seller', 'Seller'),
        ('Buyer', 'Buyer'),
    )

    user_id = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=50, choices=user_roles, default='Buyer')
    seller_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    document_verification = models.ImageField(upload_to='Documents_images', null=True, blank=True)
    gst_number = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    address_line1 = models.CharField(max_length=50, null=True, blank=True)
    address_line2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name_plural = "User"


class cart(models.Model):
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.user_id + " --> " + self.product.name + ": " + str(self.quantity)

    class Meta:
        verbose_name_plural = "Cart"


class bankDetail(models.Model):
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    accountName = models.CharField(max_length=50, null=True, blank=True)
    accountNumber = models.CharField(max_length=50, null=True, blank=True)
    accountIfsc = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.accountName + ": " + self.accountNumber

    class Meta:
        verbose_name_plural = "Bank"
