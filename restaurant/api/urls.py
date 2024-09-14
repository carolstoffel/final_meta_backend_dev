from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet

restaurant_router = DefaultRouter()
restaurant_router.register(r'menu-items', MenuItemViewSet)