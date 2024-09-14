from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.api.views import BookingViewSet

# Setting up the DefaultRouter for the BookingViewSet
router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include URLs from the restaurant app
    path('', include('restaurant.urls')),

    # Include URLs from the Little Lemon API app
    path('api/', include('littlelemon.api.urls')),

    # Include URLs for booking API with router
    path('booking/', include(router.urls)),

    # Authentication URLs for Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
