from django import contrib, forms
from django.forms import ModelForm
from .models import  Expense, Trip, Vehicle
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit



class TripAddForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['Vehicle', 'odometer_start', 'odometer_close',
                'journey_start','journey_destination','amount_collected']
        labels = {
            'Vehicle': 'Vehicle',
            'odometer_start': 'odometer start',
            'odometer_close': 'odometer close',
            'journey_start': 'journey start',
            'journey_destination': 'journey destination',
            'amount_collected': 'amount collected',
            'journey start': 'journey_start',
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.layout = Layout(
            'Vehicle',
            'odometer_start',
            'odometer_close',
            'journey_start',
            'journey_destination',
            'amount_collected',

            
        )
    
class EditTripForm(TripAddForm):
    class Meta:
        model = Trip
        fields = ['Vehicle', 'odometer_start', 'odometer_close',
                'journey_start','journey_destination','amount_collected']
        labels = {
            'Vehicle': 'Vehicle',
            'odometer_start': 'odometer start',
            'odometer_close': 'odometer close',
            'journey_start': 'journey start',
            'journey_destination': 'journey destination',
            'amount_collected': 'amount collected',
            'journey_start': 'journey_start',
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.layout = Layout(
            'Vehicle',
            'odometer_start',
            'odometer_close',
            'journey_start',
            'journey_destination',
            'amount_collected',
           
        )

class ExpenseAddForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['Vehicle', 'name', 'amount_incurred',
               ]
        labels = {
            'Vehicle': 'Vehicle',
            'name': 'Expense',
            'amount_incurred': 'Amount Incurred',
            
           
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.layout = Layout(
            'Vehicle',
            'name',
            'amount_incurred',
          
            
        )
class ExpenseEditForm(ExpenseAddForm):
    class Meta:
        model = Expense
        fields = ['Vehicle', 'name', 'amount_incurred'
                ]
        labels = {
            'Vehicle': 'Vehicle',
            'name': 'Expense',
            'amount_incurred': 'Amount Incurred',
         
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.layout = Layout(
            'Vehicle',
            'name',
            'amount_incurred',
         
            
        )        



class VehicleAddForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_reg_no', 'company', 'fleet_no']
        labels = {
            'Reg. No': 'Reg.No',
            'company': 'Company',
            'Fleet No.': 'Fleet No.',
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.layout = Layout(
            'vehicle_reg_no',
            'company',
            'fleet_no',
          
        )


class VehicleEditForm(VehicleAddForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_reg_no', 'company', 'fleet_no']
        labels = {
            'Reg. No': 'Reg.No',
            'company': 'Company',
            'Fleet No.': 'Fleet No.',
            
          
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.layout = Layout(
            'vehicle_reg_no',
            'company',
            'fleet_no',
          
        )       
