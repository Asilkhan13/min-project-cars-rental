from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Car, Client, Rental

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    paginate_by = 6
    
    def get_queryset(self):
        return Car.objects.filter(available=True)


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'


def index(request):
    cars = Car.objects.filter(available=True)[:6]
    return render(request, 'cars/index.html', {'cars': cars})


def about(request):
    return render(request, 'cars/about.html')
