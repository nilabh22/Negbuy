from django.db import models


class userDB(models.Model):
    user_roles = (
        ('Seller', 'Seller'),
        ('Buyer', 'Buyer'),
    )

    user_id = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(
        max_length=100, unique=True, null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=50, choices=user_roles, default='Buyer')
    seller_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    document_verification = models.ImageField(
        upload_to='Documents_images', null=True, blank=True)
    gst_number = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    address_line1 = models.CharField(max_length=1000, null=True, blank=True)
    address_line2 = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name_plural = "User"


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
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Inventory: " + str(self.id) + " - Capacity: " + str(self.quantity)

    class Meta:
        verbose_name_plural = "Inventory"


class product(models.Model):

    status_choice = (
        ('verified', 'verified'),
        ('under verification', 'under verification'),
    )

    price_choice = (
        ('Add Price', 'Add Price'),
        ('Price according to quantity', 'Price according to quantity')
    )

    user = models.ForeignKey(userDB, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=1000)
    sku = models.CharField(max_length=1000, null=True, blank=True)
    category_id = models.ForeignKey(
        productCategory, on_delete=models.CASCADE, null=True)
    inventory_id = models.OneToOneField(
        productInventory, on_delete=models.CASCADE, null=True)
    featured_products = models.BooleanField(default=False)
    best_selling_products = models.BooleanField(default=False)
    hot_selling_products = models.BooleanField(default=False)
    fast_dispatch = models.BooleanField(default=False)
    ready_to_ship = models.BooleanField(default=False)
    customized_product = models.BooleanField(default=False)
    brand = models.CharField(max_length=1000, null=True, blank=True)
    keyword = models.CharField(max_length=1000, null=True, blank=True)
    color = models.CharField(max_length=1000, null=True, blank=True)
    size = models.CharField(max_length=1000, null=True, blank=True)
    details = models.CharField(max_length=1000, null=True, blank=True)
    price_choice = models.CharField(
        max_length=100, choices=price_choice, null=True, blank=True)
    price = models.DecimalField(
        max_digits=12, decimal_places=4, null=True, blank=True)
    mrp = models.IntegerField(null=True, blank=True)
    sale_price = models.CharField(max_length=100, null=True, blank=True)
    sale_startdate = models.CharField(max_length=100, null=True, blank=True)
    sale_enddate = models.CharField(max_length=100, null=True, blank=True)
    manufacturing_time = models.CharField(
        max_length=100, null=True, blank=True)
    quantity_price = models.CharField(max_length=100, null=True, blank=True)
    maximum_order_quantity = models.CharField(
        max_length=100, null=True, blank=True)

    weight = models.CharField(max_length=100, null=True, blank=True)
    transportation_port = models.CharField(
        max_length=1000, null=True, blank=True)
    packing_details = models.CharField(max_length=1000, null=True, blank=True)
    packing_address = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=status_choice, default="under verification")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"


class productImages(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(
        upload_to='Product_images', default=None, blank=True)

    def __str__(self):
        return self.product.name + "--> " + str(self.image)[15:]

    class Meta:
        verbose_name_plural = "Product Image"


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
    accountName = models.CharField(max_length=1000, null=True, blank=True)
    accountNumber = models.CharField(max_length=1000, null=True, blank=True)
    accountIfsc = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.accountName + ": " + self.accountNumber

    class Meta:
        verbose_name_plural = "Bank"


class port(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    state = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name + ', ' + self.state

    class Meta:
        verbose_name_plural = "Port"


class orders(models.Model):
    order_number = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    product_info = models.ForeignKey(product, on_delete=models.CASCADE)
    order_quantity = models.CharField(max_length=1000, null=True, blank=True)
    shipping_date = models.CharField(max_length=1000, null=True, blank=True)
    delivery_date = models.CharField(max_length=1000, null=True, blank=True)
    # in future choice fields
    status = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Orders"


class contact_data(models.Model):
    message = models.CharField(max_length=1000, blank=True, null=True)
