from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company', null=True,blank=True)
    is_inspector=models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False)
    is_conductor=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'
    
class Company(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profile',null=True, blank=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:verbose_name_plural = 'Companies'

        
class Vehicle(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT,blank=True, null=True,related_name='profilevehicle')
    vehicle_reg_no = models.CharField(max_length=150,unique=True)
    fleet_no = models.CharField(max_length=150,null=True)
    created = models.DateTimeField(auto_now_add=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='vehicle',blank=True,null=True)
    
    def __str__(self):
       return f'{self.vehicle_reg_no}'
    
class Driver(models.Model):
    vehicle = models.OneToOneField(Vehicle,blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)  
    company=models.ForeignKey(Company,on_delete=models.PROTECT,related_name='driver')
    
    def __str__(self):
     return f'{self.name}' 
    
class Route(models.Model):
    route_Choices = (
            ('Nairobi-Thika', 'Nairobi-Thika'),
            ('Nairobi-Malaa', 'Nairobi-Malaa'),
            ('Nairobi-Makongeni', 'Nairobi-Makongeni'),
            
     )
    vehicle = models.OneToOneField(Vehicle, blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, choices=route_Choices)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
         return f'{self.vehicle} asssigned to  {self.name} route' 
    


class Trip(models.Model):
    journey_Choices = (
        ('Nairobi', 'Nairobi'),
        ('Thika', 'Thika'),
        ('Malaa', 'Malaa'),
        ('Makongeni', 'Makongeni'),
    )
    
   

    Vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    odometer_start = models.PositiveIntegerField()
    odometer_close = models.PositiveIntegerField()
    journey_start = models.CharField(max_length=100, choices=journey_Choices) 
    journey_destination = models.CharField(max_length=100, choices=journey_Choices) 
    amount_collected = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
   
    
    class Meta:
        ordering = ('-id',) 
    
    def __str__(self):
        return f'Trip for {self.Vehicle.vehicle_reg_no}'


    # def total_amount_collected(self):
    #  return Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum']    
        #  return Trip.objects.filter(Vehicle=self.Vehicle).aggregate(Sum('amount_collected'))['amount_collected__sum']
        # return Trip.objects.filter(Vehicle=self.Vehicle, Vehicle__owner=request.user).aggregate(Sum('amount_collected'))['amount_collected__sum']



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
    
     
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, choices=Expense_Choices) 
    amount_incurred=models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
   
    # user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='trips')
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        ordering = ('id',)

            
    def __str__(self):
        return f'Expense for {self.Vehicle.vehicle_reg_no}'
    
