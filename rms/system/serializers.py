from rest_framework import serializers
from .models import Restaurant, Menu, Order, Reservation, Review, Ingredient, Staff

from rest_framework import serializers
from .models import CustomUser




class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = ['username', 'email', 'password']
       extra_kwargs = {'password': {'write_only': True}}


   def create(self, validated_data):
       user = CustomUser(
           username=validated_data['username'],
           email=validated_data['email']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
