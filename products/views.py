# products/views.py

from typing import Any
from django.db.models.query import QuerySet
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = "products.view_post"
    template_name = "post_list.html"
    queryset = Post.objects.all()
    model = Post
    context_object_name = "posts"
    
    ordering = "-id"
    
    def get_queryset(self):
        posts = Post.objects.all()
        return posts
    
    
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = [
        "title",
        'image',
        'content',
        'status',
        ]
    success_url = "/products/post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post

    success_url = "/products/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/products/post/"

    