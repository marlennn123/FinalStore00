from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, Category, Product, ProductPhotos, Rating, Review,  Cart, CartItem
from .serializers import (
    UserProfileSerializer, CategorySerializer, ProductSerializer, ProductPhotosSerializer,
    RatingSerializer, ReviewSerializer, CartSerializer, CartItemSerializer
)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user profiles.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPhotosViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product photos.
    """
    queryset = ProductPhotos.objects.all()
    serializer_class = ProductPhotosSerializer


class RatingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product ratings.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




class CartViewSet(viewsets.ViewSet):
    """
    A viewset for managing the shopping cart.
    """

    def list(self, request):
        try:
            user_profile = request.user.userprofile  # Assuming UserProfile is linked to User model
            cart, created = Cart.objects.get_or_create(user=user_profile)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def add(self, request):
        try:
            user_profile = request.user.userprofile  # Assuming UserProfile is linked to User model
            cart, created = Cart.objects.get_or_create(user=user_profile)
            product_id = request.data.get('product_id')
            quantity = request.data.get('quantity', 1)

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def remove(self, request):
        try:
            user_profile = request.user.userprofile  # Assuming UserProfile is linked to User model
            cart, created = Cart.objects.get_or_create(user=user_profile)
            product_id = request.data.get('product_id')

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            try:
                cart_item = CartItem.objects.get(cart=cart, product=product)
                cart_item.delete()
            except CartItem.DoesNotExist:
                return Response({"error": "Product not in cart"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"message": "Product removed from cart"}, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def clear(self, request):
        try:
            user_profile = request.user.userprofile  # Assuming UserProfile is linked to User model
            cart, created = Cart.objects.get_or_create(user=user_profile)
            cart.items.all().delete()
            return Response({"message": "Cart cleared"}, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)