from rest_framework import serializers
from .models import CustomUser, Employee, Supply, Feedback, Booking, CustomerOrder, MenuItem, Diner

class UserSerializer(serializers.ModelSerializer):
    # Password is write-only and should not be included in read operations
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a user instance with the validated data
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        # Set the password using the set_password method to hash it properly
        user.set_password(validated_data['password'])
        user.save()
        return user

class DinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diner
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
