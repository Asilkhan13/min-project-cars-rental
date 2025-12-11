from django.contrib import admin
from .models import Car, Client, Rental

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price_per_day', 'available']
    list_filter = ['available', 'year']
    search_fields = ['brand', 'model']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone', 'email']


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['car', 'client', 'start_date', 'end_date', 'status', 'total_price']
    list_filter = ['status', 'start_date']
    search_fields = ['client__name', 'car__brand']
