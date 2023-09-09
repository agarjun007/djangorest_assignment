from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    id = models.AutoField(db_column="id", primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'auth_users'


class Products(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Users, db_column="customer_id", related_name="customer_products", on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.0, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'products'
