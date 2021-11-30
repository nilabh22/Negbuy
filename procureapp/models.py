from django.db import models

# Create your models here.

class Procurement_User(models.Model):

    user_roles = (
        ('Merchant','Merchant'),
        ('Buyer','Buyer'),
    )

    user_id = models.CharField(max_length=1000, null=True, blank=True)
    username = models.CharField(max_length=1000, unique=True)
    first_name = models.CharField(max_length=1000, null=True, blank=True)
    last_name = models.CharField(max_length=1000, null=True, blank=True)
    role = models.CharField(max_length=1000, choices=user_roles, default='Buyer')
    address_line1 = models.CharField(max_length=1000, null=True, blank=True)
    address_line2 = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=1000, null=True, blank=True)
    postal_code = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=1000, null=True, blank=True)
    telephone = models.CharField(max_length=1000, null=True, blank=True)
    mobile = models.CharField(max_length=1000, null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=True)
    organization = models.CharField(max_length=1000, null=True, blank=True)


class Generated_RFQ(models.Model):

    category_choices = (
        ('Mechanical','Mechanical'),
        ('Electrical','Electrical'),
        ('Other','Other'),
    )

    RFQ_choices = (
        ('SI','SI'),
        ('NSI','NSI'),
    )

    user = models.ForeignKey(Procurement_User, on_delete=models.CASCADE, null=True)
    Category = models.CharField(max_length=1000, choices=category_choices, default='Mechanical', null=True, blank=True)
    RFQ_type = models.CharField(max_length=1000, choices=RFQ_choices, default='SI', null=True, blank=True)
    Item_name = models.CharField(max_length=1000, null=True, blank=True)
    Quantity = models.CharField(max_length=1000, null=True, blank=True)
    Model_Information = models.CharField(max_length=1000, null=True, blank=True)
    Delivery_Time_Duration = models.CharField(max_length=1000, null=True, blank=True)
    Price_Range = models.CharField(max_length=1000, null=True, blank=True)
    RFQ_image = models.ImageField(upload_to='RFQ', default=None, blank=True)
