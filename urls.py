from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('car/<int:car_id>/rent/', views.RentalCreateView.as_view(), name='rental_create'),
    path('rental/success/', views.rental_success, name='rental_success'),
    path('about/', views.about, name='about'),
]
