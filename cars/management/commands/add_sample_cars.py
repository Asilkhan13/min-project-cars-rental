from django.core.management.base import BaseCommand
from cars.models import Car
from django.core.files import File
from django.core.files.images import ImageFile
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Добавляет примеры машин в базу данных'

    def handle(self, *args, **options):
        cars_data = [
            {
                'name': 'Toyota Camry',
                'brand': 'Toyota',
                'model': 'Camry',
                'year': 2023,
                'price_per_day': 25000,
                'transmission': 'automatic',
                'seats': 5,
                'description': 'Комфортный седан для семейных поездок. Экономичный расход топлива.',
                'available': True,
                'image_path': 'cars/toyota_camry.jpg'
            },
            {
                'name': 'Hyundai Tucson',
                'brand': 'Hyundai',
                'model': 'Tucson',
                'year': 2023,
                'price_per_day': 30000,
                'transmission': 'automatic',
                'seats': 5,
                'description': 'Надежный кроссовер с хорошей проходимостью.',
                'available': True,
            },
            {
                'name': 'BMW 3 Series',
                'brand': 'BMW',
                'model': '3 Series',
                'year': 2022,
                'price_per_day': 40000,
                'transmission': 'automatic',
                'seats': 5,
                'description': 'Премиум седан для деловых людей и особых поводов.',
                'available': True,
            },
            {
                'name': 'Kia Sportage',
                'brand': 'Kia',
                'model': 'Sportage',
                'year': 2023,
                'price_per_day': 27500,
                'transmission': 'automatic',
                'seats': 5,
                'description': 'Стильный кроссовер с современным дизайном.',
                'available': True,
            },
            {
                'name': 'Chevrolet Aveo',
                'brand': 'Chevrolet',
                'model': 'Aveo',
                'year': 2022,
                'price_per_day': 17500,
                'transmission': 'manual',
                'seats': 5,
                'description': 'Экономный седан для городских поездок.',
                'available': True,
            },
            {
                'name': 'Mercedes-Benz C-Class',
                'brand': 'Mercedes-Benz',
                'model': 'C-Class',
                'year': 2023,
                'price_per_day': 50000,
                'transmission': 'automatic',
                'seats': 5,
                'description': 'Люксовый седан премиум-класса с полной комплектацией.',
                'available': True,
            },
        ]

        for car_data in cars_data:
            car, created = Car.objects.get_or_create(
                brand=car_data['brand'],
                model=car_data['model'],
                year=car_data['year'],
                defaults={k: v for k, v in car_data.items() if k != 'image_path'}
            )
            
            # Загрузить фото если оно существует
            if 'image_path' in car_data and not car.image:
                image_full_path = Path('media') / car_data['image_path']
                if image_full_path.exists():
                    with open(image_full_path, 'rb') as img_file:
                        car.image.save(car_data['image_path'], ImageFile(img_file))
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Добавлена машина: {car}'))
            else:
                self.stdout.write(self.style.WARNING(f'Машина уже существует: {car}'))
