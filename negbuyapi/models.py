from django.db import models

# Create your models here.

class User_db(models.Model):

    User_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('other', 'other'),
    )

    language_choices = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
    )

    user_id = models.CharField(max_length=100, unique=True , null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=50,unique=True, null=True, blank=True)
    email = models.CharField(max_length=100,unique=True, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=User_gender, null=True, blank=True)
    language = models.CharField(max_length=100,choices=language_choices, default='English', null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user_id
    class Meta:
        verbose_name_plural = "User db"

class Merchant_db(models.Model):

    User_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('other', 'other'),
    )

    language_choices = (
        ('English', 'English'),
        ('Hindi', 'Hindi'),
    )

    user_id = models.CharField(max_length=100, unique=True , null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.CharField(max_length=50,unique=True, null=True, blank=True)
    email = models.CharField(max_length=100,unique=True, null=True, blank=True)
    gender = models.CharField(max_length=100,choices=User_gender, null=True, blank=True)
    language = models.CharField(max_length=100, choices=language_choices, default='English', null=True, blank=True)
    location = models.CharField(max_length=1000, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user_id
    class Meta:
        verbose_name_plural = "Merchant db"

class Product_db(models.Model):

    fast_dispatch_choices = (
        ('True','True'),
        ('False','False')
    )

    user_id = models.ForeignKey(Merchant_db, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    category = models.CharField(max_length=2000, null=True, blank=True)  #in future a choice field
    image = models.ImageField(upload_to='Product_images', default=None, blank=True)
    fast_dispatch = models.CharField(max_length=100, choices=fast_dispatch_choices, null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Product db"