from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.api.urls import restaurant_router
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.registry.extend(restaurant_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]