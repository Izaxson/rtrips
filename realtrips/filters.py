import django_filters
from django_filters import DateFilter
from realtrips.models import Trip ,Expense, Vehicle


# steps from here to use the filter library: https://github.com/carltongibson/django-filter
# https://django-filter.readthedocs.io/en/main/

class TripFilter(django_filters.FilterSet):    
    start_date=DateFilter(field_name="created", lookup_expr='gte') 
    end_date=DateFilter(field_name="created", lookup_expr='lte') 
    class Meta:
        model = Trip
        fields = '__all__'
        # exclude = ['odometer_start','odometer_close','profile','amount_collected','created',]
        # fields = ['Vehicle', 'odometer_start', 'odometer_close','journey_start', 'journey_destination','amount_collected','profile' ]
         

class ExpenseFilter(django_filters.FilterSet):  
    start_date=DateFilter(field_name="created", lookup_expr='gte') 
    end_date=DateFilter(field_name="created", lookup_expr='lte')    
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['profile','created','amount_incurred','journey_start','journey_destination']



class ReportFilter(django_filters.FilterSet):  
    start_date=DateFilter(field_name="created", lookup_expr='gte') 
    end_date=DateFilter(field_name="created", lookup_expr='lte')    
    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ['odometer_start','odometer_close','profile','amount_collected','created',]  

class VehicleFilter(django_filters.FilterSet):  
    
    class Meta:
        model = Vehicle
        fields = ['vehicle_reg_no', 'company', 'fleet_no']
        