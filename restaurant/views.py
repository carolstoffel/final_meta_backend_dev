from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Booking
from .forms import BookingForm
from django.core import serializers
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Home page view
def home(request):
    return render(request, 'index.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Menu item list view
def menu_item(request):
    menu_data = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu': menu_data})

# Display a specific menu item view
def display_menu_item(request, pk=None):
    menu_item = get_object_or_404(MenuItem, pk=pk) if pk else None
    return render(request, 'menu_item.html', {'menu_item': menu_item})

# Booking form view
def book(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Optionally redirect to a success page or show a success message
    return render(request, 'book.html', {'form': form})

# Reservations view (for displaying bookings)
def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})

# Bookings API endpoint view
@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        reservation_date = data.get('reservation_date')
        reservation_slot = data.get('reservation_slot')

        if not reservation_date or not reservation_slot:
            return JsonResponse({'error': 'Missing data'}, status=400)

        exist = Booking.objects.filter(
            reservation_date=reservation_date,
            reservation_slot=reservation_slot
        ).exists()

        if not exist:
            Booking.objects.create(
                first_name=data.get('first_name'),
                reservation_date=reservation_date,
                reservation_slot=reservation_slot
            )
            return JsonResponse({'status': 'Booking created'}, status=201)
        else:
            return JsonResponse({'error': 'Slot already reserved'}, status=400)

    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type='application/json')
