from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

#create a custom user model if needed
# This is optional but can be useful for extending user functionality in the future.
class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This can be used to add additional fields or methods in the future.
    """
    # Add any additional fields here if needed
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    
class Product(models.Model):
    """
    Model representing a product in the e-commerce store.
    """
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    size = models.CharField(max_length=50, blank=True, null=True)
    
class Order(models.Model):
    """
    Model representing an order placed by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
class contact(models.Model):
    """
    Model representing a contact message from a user.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    
class user_profile(models.Model):
    """
    Model representing a user profile.
    """
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)

