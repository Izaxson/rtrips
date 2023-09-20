from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Vehicle(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_reg_no = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateField()
    
    
    def __str__(self):
        return self.vehicle_reg_no

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)

class Trip(models.Model):
    journey_Choices = (
             ('Nairobi-Thika', 'Nairobi-Thika'),
            ('Nairobi-Malaa', 'Nairobi-Malaa'),
            ('Nairobi-Makongeni', 'Nairobi-Makongeni'),
     )
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    odometer_start=models.PositiveIntegerField()
    odometer_close=models.PositiveIntegerField()
    time=models.TimeField(auto_now=False, auto_now_add=False)
    journey_start=models.CharField(max_length=100, choices=journey_Choices) 
    journey_destination=models.CharField(max_length=100, choices=journey_Choices) 
    amount_collected=models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated=models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return f'Trip for {self.Vehicle.vehicle_reg_no}'
    def total_amount_collected(self):
     return Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum'] 
   
class Expense(models.Model):
    Expense_Choices = (
            ('FUEL-DIESEL', 'Fuel-Diesel'),
            ('BREAKFAST', 'Breakfast'),
            ('Lunch', 'Lunch'),
            ('Salaries', 'Salaries'),
            ('Parking Fee', 'Parking Fee'),
            ('Line', 'Line'),
            ('Boys', 'Boys'),
            ('Car Wash', 'Car Wash'),
            ('Oil/CC', 'Oil/CC'),
            ('Puncher', 'Puncher'),
            ('BREAKFAST', 'Breakfast'),
            ('Services', 'Services'),
            ('Greasing', 'Greasing'),
            ('Pad', 'Pad'),
            ('Garage', 'Garage'),
            ('Spare', 'Spare'),
            ('Tyre', 'Tyre'),
            ('Batteries', 'Batteries'),
            ('Break Fluid', 'Break Fluid'),
            ('Others', 'Others'),
        )   
     
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=Expense_Choices) 
    amount_incurred=models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated=models.DateTimeField(auto_now=False)
   

    def __str__(self):
        return f'Expense for {self.Vehicle.vehicle_reg_no}'
    
class Route(models.Model):
    Route_choice = (
            ('Nairobi-Thika', 'Nairobi-Thika'),
            ('Nairobi-Malaa', 'Nairobi-Malaa'),
            ('Nairobi-Makongeni', 'Nairobi-Makongeni'),
           

    )
    Vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    route = models.CharField(max_length=100, choices=Route_choice, default='Nairobi-Thika')
    created = models.DateField()
    
    
    def __str__(self):
        # return self.route    
        return f'Route assigned to {self.Vehicle.vehicle_reg_no}'