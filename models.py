from django.db import models
from django.utils import timezone

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('automatic', 'Автоматическая'),
        ('manual', 'Механическая'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Название")
    brand = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена в день")
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, verbose_name="КПП")
    seats = models.IntegerField(verbose_name="Количество мест")
    image = models.ImageField(upload_to='cars/', verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")
    available = models.BooleanField(default=True, verbose_name="Доступна")
    
    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    passport = models.CharField(max_length=20, verbose_name="Паспорт")
    driver_license = models.CharField(max_length=20, verbose_name="Водительское удостоверение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
    
    def __str__(self):
        return self.name


class Rental(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('active', 'Активна'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]
    
    car = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name="Автомобиль")
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name="Клиент")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(verbose_name="Дата окончания")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Аренда"
        verbose_name_plural = "Аренды"
    
    def __str__(self):
        return f"{self.car} - {self.client} ({self.start_date.date()})"
    
    def calculate_total_price(self):
        days = (self.end_date - self.start_date).days
        if days <= 0:
            days = 1
        return self.car.price_per_day * days
