from django.db import models
from user.models import User
from django.urls import reverse

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
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("products:post-detail", kwargs={"pk": self.pk})