from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
   path('register/', register_user, name='register'),
   path('login/', user_login, name='login'),
   path('logout/', user_logout, name='logout'),
]


router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
