

from django.urls import path,include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'products'


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path("post/", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit/",views.PostUpdateView.as_view(),name="post_edit"),
    path("post/<int:pk>/delete/",views.PostDeleteView.as_view(),name="post_delete"),
    
]
