from django.db import models
from django.utils.timezone import timezone
<<<<<<< HEAD
from django.core.validators import FileExtensionValidator
=======
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5


class userDB(models.Model):
    user_roles = (
        ('Seller', 'Seller'),
        ('Buyer', 'Buyer'),
    )

    user_id = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(
        max_length=100, unique=True, null=True, blank=True)
<<<<<<< HEAD
    password = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_images', default=None, blank=True, null=True)
=======
    password = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
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
<<<<<<< HEAD
        return f"{self.seller_name}   |   {self.phone}"

    class Meta:
        verbose_name_plural = "Users"
=======
        return f"{self.user_id} | {self.phone}"

    class Meta:
        verbose_name_plural = "User"
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5


class productCategory(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Category"


<<<<<<< HEAD
# class productInventory(models.Model):
#     quantity = models.PositiveIntegerField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "Inventory: " + str(self.id) + " --- Capacity: " + str(self.quantity)

#     class Meta:
#         verbose_name_plural = "Inventory"
=======
class productInventory(models.Model):
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Inventory: " + str(self.id) + " - Capacity: " + str(self.quantity)

    class Meta:
        verbose_name_plural = "Inventory"
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5


class product(models.Model):

<<<<<<< HEAD
    page_no = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
=======
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
    status_choice = (
        ('verified', 'verified'),
        ('under verification', 'under verification'),
    )

    price_choice = (
        ('Add Price', 'Add Price'),
<<<<<<< HEAD
        ('Price according to quantity', 'Price according to quantity'),
    )

    user = models.ForeignKey(
        userDB, on_delete=models.SET_NULL, null=True, related_name='user')
=======
        ('Price according to quantity', 'Price according to quantity')
    )

    user = models.ForeignKey(userDB, on_delete=models.SET_NULL, null=True)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
    name = models.CharField(max_length=1000)
    sku = models.CharField(max_length=1000, null=True, blank=True)
    category_id = models.ForeignKey(
        productCategory, on_delete=models.CASCADE, null=True)
<<<<<<< HEAD
    sub_category = models.CharField(max_length=1000, null=True, blank=True)
    # inventory_id = models.OneToOneField(
    #     productInventory, on_delete=models.SET_NULL, null=True)
=======
    inventory_id = models.OneToOneField(
        productInventory, on_delete=models.CASCADE, null=True)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
    main_image = models.ImageField(
        upload_to='main_images', default=None, blank=True, null=True)
    featured_products = models.BooleanField(default=False)
    best_selling_products = models.BooleanField(default=False)
    hot_selling_products = models.BooleanField(default=False)
<<<<<<< HEAD
    varients = models.BooleanField(default=False)
=======
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
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
<<<<<<< HEAD
        max_digits=12, decimal_places=2, null=True, blank=True)
=======
        max_digits=12, decimal_places=4, null=True, blank=True)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
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
<<<<<<< HEAD
    page_status = models.CharField(
        max_length=100, choices=page_no, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='product_videos', null=True, blank=True)
    detailed_description = models.TextField(
        max_length=15000, null=True, blank=True)
=======
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5

    def __str__(self):
        return self.name

    class Meta:
<<<<<<< HEAD
        verbose_name_plural = "Products"
=======
        verbose_name_plural = "Product"
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5


class productImages(models.Model):
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name='product_images', null=True)
    image = models.ImageField(
        upload_to='Product_images', default=None, blank=True)
<<<<<<< HEAD
    main_image = models.BooleanField(default=False)
    size = models.CharField(max_length=1000, null=True, blank=True)
    color = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Product Images"
=======

    def __str__(self):
        return self.product.name + "--> " + str(self.image)[15:]

    class Meta:
        verbose_name_plural = "Product Image"
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5


class cart(models.Model):

    status_choice = (
        ('Running', 'Running'),
        ('Completed', 'Completed'),
    )

    order_number = models.PositiveIntegerField(null=True, blank=False)
    buyer_info = models.ForeignKey(userDB, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField(null=True, blank=True)
    order_price = models.DecimalField(
        null=True, blank=True, decimal_places=4, max_digits=12)
    logistics_charges = models.DecimalField(
        null=True, decimal_places=4, max_digits=12)
    total_price = models.DecimalField(
        null=True, blank=True, decimal_places=4, max_digits=12)
    order_date = models.CharField(max_length=20, null=True, blank=True)
    order_status = models.CharField(
        max_length=1000, null=True, blank=True, choices=status_choice)
    order_note = models.CharField(max_length=1000, null=True, blank=True)
    billing_address = models.TextField(max_length=1000, null=True, blank=True)
    billing_landmark = models.CharField(max_length=100, null=True, blank=True)
    billing_zipcode = models.CharField(max_length=100, null=True, blank=True)
    billing_city = models.CharField(max_length=1000, null=True, blank=True)
    billing_state = models.CharField(max_length=1000, null=True, blank=True)
    billing_country = models.CharField(max_length=1000, null=True, blank=True)
    shipping_adress = models.TextField(max_length=1000, null=True, blank=True)
    shipping_landmark = models.CharField(
        max_length=100, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=100, null=True, blank=True)
    shipping_city = models.CharField(max_length=1000, null=True, blank=True)
    shipping_state = models.CharField(max_length=1000, null=True, blank=True)
    shipping_country = models.CharField(max_length=1000, null=True, blank=True)

<<<<<<< HEAD
=======
    def __str__(self):
        return self.user.user_id + " --> " + self.product.name + ": " + str(self.quantity)

>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
    class Meta:
        verbose_name_plural = "Cart"


class bankDetail(models.Model):
<<<<<<< HEAD
    user = models.ForeignKey(
        userDB, on_delete=models.CASCADE, related_name='user_bankDetails')
=======
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
    accountName = models.CharField(max_length=1000, null=True, blank=True)
    accountNumber = models.CharField(max_length=1000, null=True, blank=True)
    accountIfsc = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Bank"


class port(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=1000, null=True, blank=True)
    latitude = models.CharField(max_length=1000, null=True, blank=True)
    longitude = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Port"


class orders(models.Model):

    status_choice = (
        ('Running', 'Running'),
        ('Completed', 'Completed'),
    )

    order_number = models.CharField(max_length=1000, null=True, blank=True)
    order_date = models.DateTimeField(auto_now=True, null=True)
    order_time = models.TimeField(auto_now_add=False, null=True)
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    product_info = models.ForeignKey(product, on_delete=models.CASCADE)
    order_quantity = models.CharField(max_length=1000, null=True, blank=True)
    shipping_date = models.CharField(max_length=1000, null=True, blank=True)
    delivery_date = models.CharField(max_length=1000, null=True, blank=True)
    # in future choice fields
    status = models.CharField(
        max_length=1000, null=True, blank=True, choices=status_choice)
<<<<<<< HEAD
    feedback = models.TextField(max_length=1000, null=True, blank=True)
    order_note = models.CharField(max_length=1000, null=True, blank=True)
=======
    feedback = models.CharField(max_length=1000, null=True, blank=True)
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Orders"


class contact_data(models.Model):
    message = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact Data"


class primary_category(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    prod_category = models.ManyToManyField('productCategory')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Primary Category"


<<<<<<< HEAD
class review_db(models.Model):

    rating_choices = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(
        userDB, on_delete=models.CASCADE)
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name='reviews')
    review_title = models.CharField(max_length=1000, null=True, blank=True)
    review = models.CharField(max_length=1000, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "Product Reviews"


class product_detail_db(models.Model):
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name='image_details')
    image = models.ImageField(
        upload_to='New_Images', default=None, blank=True)
    heading = models.CharField(max_length=1000, null=True, blank=True)
    desc = models.CharField(max_length=10000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Product Details"


class Inventory(models.Model):
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name='inventory_product')
    quantity = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length=1000, null=True, blank=True)
    size = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Inventory"


class rfq(models.Model):
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True)
    target_price = models.IntegerField(blank=True, null=True)
    quantity = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "RFQs"
=======
class rfq_db(models.Model):
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    required =models.CharField(max_length=1000, blank=True, null=True)  # change the name .....requirement
    date = models.DateTimeField(auto_now=True, null=True)
    target_price = models.IntegerField( blank=True, null=True) 
    # add the quantity
    # then make the get api and return  the list value of all the object 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.first_name) + str(self.user.last_name)

    class Meta:
        verbose_name_plural = "RFQ_db"

class rfq(models.Model):
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    requirement =models.CharField(max_length=1000, blank=True, null=True)  
    date = models.DateTimeField(auto_now=True, null=True)
    target_price = models.IntegerField( blank=True, null=True)
    quantity = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.first_name) + str(self.user.last_name)

    class Meta:
        verbose_name_plural = "rfq"


class buyer_questions(models.Model):
    user = models.ForeignKey(userDB, on_delete=models.CASCADE)
    product =  models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    question =models.CharField(max_length=1000, blank=True, null=True)
    feedback= models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.question
        # return str(self.user.first_name) + str(self.user.last_name)

    class Meta:
        verbose_name_plural = "Buyer_Questions"
>>>>>>> c571916195af49b2171c76e667617a10b583c0a5
