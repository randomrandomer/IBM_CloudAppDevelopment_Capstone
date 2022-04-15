from django.db import models
from django.utils.timezone import now
from django.core import serializers 
import uuid
import json

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=True, max_length=30, default='Add name here')
    description = models.CharField(null=True,  max_length=30, default='Add description here')

    def __str__(self):
        return 'Name: ' + self.name + "," + \
            'Description: ' + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):

    SEDAN = 'Sedan'
    SUV = 'Suv'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    SPORTS = 'Sports'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    MINIVAN = 'Minivan'
    Type_Choice = [
        (SEDAN, 'Sedan'), 
        (SUV, 'Suv'), 
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (SPORTS, 'Sports'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
        (MINIVAN, 'Minivan'),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=30, default='name')
    id = models.IntegerField(default=0, primary_key=True)
    type = models.CharField(null=True, max_length=30, choices=Type_Choice, default=SEDAN)
    year = models.DateField(null=True)
    
    def __str__(self):
        return 'Title: ' + self.type

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, full_name ,short_name, st, address, city,  id, lat, long, state, zip):
        
        # Dealer Full Name
        self.full_name = full_name        
        # Dealer short name
        self.short_name = short_name
        # short_name
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer state
        self.state = state
        # State Code
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:
        def __init__(self, id, dealership, name, purchase, purchase_date, car_make, car_model, car_year, review, sentiment):

            self.dealership = dealership
            self.name = name
            self.purchase_date = purchase_date
            self.review = review
            self.purchase = purchase
            self.car_make = car_make
            self.car_model = car_model
            self.car_year = car_year
            self.sentiment = sentiment
            self.id = id
        
        def __str__(self):
                return "Review: " + self.review

        def to_json(self):
                return json.dumps(self, default=lambda o: o.__dict__,
                                  sort__keys=True, indent=4)
                                


class ReviewPost:

    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)