from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product,Post
# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     models 
admin.site.register(Product)
admin.site.register(Post)