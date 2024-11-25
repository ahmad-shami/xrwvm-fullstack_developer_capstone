# Uncomment the following imports before adding the Model code

# from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make
    country = models.CharField(max_length=50, blank=True, null=True)  # Optional: Country of origin

    def __str__(self):
        return f"{self.name} - {self.description}"

class CarModel(models.Model):
    TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Wagon', 'Wagon'),
        ('Truck', 'Truck'),
        ('Coupe', 'Coupe'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-one relationship
    dealer_id = models.IntegerField()  # Refers to a dealer ID in Cloudant
    name = models.CharField(max_length=100)  # Name of the car model
    car_type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # Type of the car
    year = models.IntegerField()  # Manufacturing year
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional: Price

    def __str__(self):
    # Match the object creation structure for consistent representation
      return f"CarModel(name='{self.name}', car_type='{self.car_type}', year={self.year}, make='{self.make.name}')"

      