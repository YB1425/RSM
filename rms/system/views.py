from rest_framework import viewsets
from .models import Restaurant, Menu, Order, Reservation, Review, Ingredient, Staff
from .serializers import (
    RestaurantSerializer, MenuSerializer, OrderSerializer,
    ReservationSerializer, ReviewSerializer, IngredientSerializer, StaffSerializer
)

from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status




@api_view(['POST'])
def register_user(request):
   if request.method == 'POST':
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def user_login(request):
   if request.method == 'POST':
       username = request.data.get('username')
       password = request.data.get('password')


       user = None
       if '@' in username:
           try:
               user = CustomUser.objects.get(email=username)
           except ObjectDoesNotExist:
               pass


       if not user:
           user = authenticate(username=username, password=password)


       if user:
           token, _ = Token.objects.get_or_create(user=user)
           return Response({'token': token.key}, status=status.HTTP_200_OK)


       return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
   if request.method == 'POST':
       try:
           # Delete the user's token to logout
           request.user.auth_token.delete()
           return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
