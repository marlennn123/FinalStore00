from rest_framework import serializers
from .models import UserProfile, Category, Product, ProductPhotos, Rating, Review, Cart, CartItem

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'age', 'date_registered', 'email', 'phone_number', 'status']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RatingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Rating
        fields = ['product', 'user', 'stars']

class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields = ['author', 'text', 'product', 'parent_review', 'created_date']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'category', 'price', 'description', 'date', 'active', 'ratings', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class ProductPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = ['product', 'image']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'items']
