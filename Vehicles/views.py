from django.http import HttpResponse
from django.shortcuts import render
from Vehicles.models import Expense, Trip
from django.views.generic import ListView  ,DetailView
# Create your views here.

class TripListView(ListView):
    model = Trip
    template_name = 'Vehicles/home.html' # name of your home template
    paginate_by=5

# def dashboard(request):
#     return render (request, 'vehicles/dashboard.html')
    

class ExpenseListView(ListView):
    model = Expense
    template_name = 'Vehicles/expense.html' # name of your home template
    paginate_by=5    


from django.shortcuts import render
from django.views.generic import ListView
from .models import Trip, Expense
from django.db.models import Sum, F

class NetRevenuePerVehicleListView(ListView):
    model = Trip
    template_name = 'net_revenue_per_vehicle.html'
    context_object_name = 'trips_and_expenses'

    def get_queryset(self):
        vehicle_registration_number = self.kwargs['vehicle_registration_number']
        date = self.kwargs['date']
        queryset = Trip.objects.filter(Vehicle__vehicle_reg_no=vehicle_registration_number, created__date=date)
        queryset = queryset.select_related('Vehicle')
        queryset = queryset.annotate(total_collections=Sum('amount_collected'), total_expenses=Sum('expense__amount_incurred'))
        queryset = queryset.annotate(net_revenue=F('total_collections') - F('total_expenses'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle_registration_number = self.kwargs['vehicle_registration_number']
        date = self.kwargs['date']
        context['vehicle_registration_number'] = vehicle_registration_number
        context['date'] = date
        return context
