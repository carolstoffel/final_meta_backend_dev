from django.urls import path
from .views import home, about, menu_item, display_menu_item, book, reservations, bookings

urlpatterns = [
    # Home page
    path('', home, name="home"),

    # About page
    path('about/', about, name="about"),

    # Menu item list
    path('menu/', menu_item, name='menu'),

    # Specific menu item details
    path('menu_item/<int:pk>/', display_menu_item, name="menu_item"),

    # Booking form
    path('book/', book, name="book"),

    # Reservations list
    path('reservations/', reservations, name="reservations"),

    # Bookings API endpoint
    path('bookings/', bookings, name='bookings'), 
]
