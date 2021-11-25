from django.db import models

# Create your models here.


class procure_userdb(models.Model):

    user_roles = (
        ('Merchant', 'Merchant'),
        ('Buyer', 'Buyer'),
    )

    id = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=user_roles, default='Buyer')
    telephone = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "procure_user_db"
