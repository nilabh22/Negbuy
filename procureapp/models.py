from django.db import models


class procurementUser(models.Model):

    user_roles = (
        ('Merchant', 'Merchant'),
        ('Buyer', 'Buyer'),
    )

    user_id = models.CharField(max_length=1000, null=True, blank=True)
    first_name = models.CharField(max_length=1000, null=True, blank=True)
    last_name = models.CharField(max_length=1000, null=True, blank=True)
    role = models.CharField(max_length=1000, choices=user_roles, default='Buyer')
    country = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=1000, null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=True)
    organization = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user_id


class generatedRFQ(models.Model):

    category_choices = (
        ('Mechanical', 'Mechanical'),
        ('Electrical', 'Electrical'),
        ('Other', 'Other'),
    )

    RFQ_choices = (
        ('SI', 'SI'),
        ('NSI', 'NSI'),
    )

    rfq_status_choices = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )

    user = models.ForeignKey(procurementUser, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=1000, choices=category_choices, default='Mechanical', null=True, blank=True)
    rfq_type = models.CharField(max_length=1000, choices=RFQ_choices, default='SI', null=True, blank=True)
    item_name = models.CharField(max_length=1000, null=True, blank=True)
    quantity = models.CharField(max_length=1000, null=True, blank=True)
    model_information = models.CharField(max_length=1000, null=True, blank=True)
    delivery_time_duration = models.CharField(max_length=1000, null=True, blank=True)
    price_range = models.CharField(max_length=1000, null=True, blank=True)
    rfq_image = models.ImageField(upload_to='RFQ', default=None, blank=True)
    rfq_status = models.CharField(max_length=1000, choices=rfq_status_choices, default='Pending', null=True, blank=True)
    datetime = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.user_id + ": " + self.category + " (" + self.rfq_type + ")"
