from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Car, Client, Rental
from .forms import RentalForm, ClientForm

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


class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    template_name = 'cars/rental_form.html'
    success_url = reverse_lazy('rental_success')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_id = self.kwargs.get('car_id')
        context['car'] = get_object_or_404(Car, id=car_id)
        return context


def rental_success(request):
    return render(request, 'cars/rental_success.html')


def about(request):
    return render(request, 'cars/about.html')
