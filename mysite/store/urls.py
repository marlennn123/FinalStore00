from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserProfileViewSet, CategoryViewSet, ProductViewSet, ProductPhotosViewSet, RatingViewSet, \
    ReviewViewSet, CartViewSet

urlpatterns = [
    path('userprofiles/', UserProfileViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='userprofile-list'),
    path('userprofiles/<int:pk>/', UserProfileViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='userprofile-detail'),

    path('categories/', CategoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='category-list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='category-detail'),

    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='product-detail'),

    path('productphotos/', ProductPhotosViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='productphotos-list'),
    path('productphotos/<int:pk>/', ProductPhotosViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='productphotos-detail'),

    path('ratings/', RatingViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='rating-list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='rating-detail'),

    path('reviews/', ReviewViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='review-list'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='review-detail'),

    path('carts/', CartViewSet.as_view({
        'get': 'list',
    }), name='carts-list'),
    path('carts/<int:pk>/', CartViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='carts-detail'),
]


