from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    register_user, user_login, user_logout,
    RestaurantViewSet, MenuViewSet, OrderViewSet,
    ReservationViewSet, ReviewViewSet, IngredientViewSet, StaffViewSet,reset_password
)

# Initialize the default router
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'staff', StaffViewSet)

# Combine all urlpatterns into a single list
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('reset-password/', reset_password, name='reset_password'),

    path('', include(router.urls)),
]
