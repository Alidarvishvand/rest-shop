from django.db import models
from user.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    # author = models.ForeignKey("user.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField()
    
    
    def __str__(self):
        return self.title