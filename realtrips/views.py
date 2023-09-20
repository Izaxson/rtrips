from collections import UserDict
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from realtrips.models import Expense, Trip,Driver, Vehicle
from django.views.generic import ListView  ,DetailView , CreateView ,FormView ,UpdateView
from django.db.models import Sum
from django.contrib import messages
from .forms import  EditTripForm, ExpenseEditForm, TripAddForm ,ExpenseAddForm , VehicleAddForm ,VehicleEditForm
from django.contrib.auth.decorators import login_required, permission_required
from .filters import TripFilter,ExpenseFilter, VehicleFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_filters.views import FilterView
from django.db.models import Q





class ExpenseListView(LoginRequiredMixin, FilterView):
    model = Expense
    template_name = 'realtrips/expense.html'
    filterset_class = ExpenseFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(profile=self.request.user.profile)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name=search_query) ,
                Q(Vehicle__icontains=search_query)
            )

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

class VehicleListView(LoginRequiredMixin, FilterView):
    model = Vehicle
    template_name = 'realtrips/vehicle.html'
    filterset_class = VehicleFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.filter(profile=self.request.user.profile)

        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name=search_query) ,
                Q(Vehicle__icontains=search_query)
            )

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context   
    
class TripListView(LoginRequiredMixin, FilterView):
    model = Trip
    template_name = 'realtrips/trips.html'
    filterset_class = TripFilter

    

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(profile=self.request.user.profile)  #'profile' is the ForeignKey to the 'Profile' model
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate mileage for each trip
        trips = context['object_list']
        for trip in trips:
            trip.mileage = trip.odometer_close - trip.odometer_start

        context['filter'] = self.filterset
        return context



class DashboardView(LoginRequiredMixin,ListView):
    model= Trip
    template_name = 'realtrips/dashboard.html' # name of your home template
    def total_amount_collected(self):
        return Trip.objects.aggregate(Sum('amount_collected'))['amount_collected_sum']

    def form_valid(self, form):
        form.save()

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Trip.objects.all()
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate the total amount collected
        total_amount_collected = Trip.objects.aggregate(Sum('amount_collected')).get('amount_collected__sum')
        context['total_amount_collected'] = total_amount_collected
            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred

         # Calculate the Net revenue

        # context['net_revenue'] = Trip.objects.aggregate(net_revenue=Sum('amount_collected__sum') - Sum('amount_incurred__sum'))
        # net_revenue = total_amount_collected - total_expense_incurred
        # context['net_revenue'] = net_revenue
        net_revenue = total_amount_collected - total_expense_incurred
        context['net_revenue'] = net_revenue


        # Calculate trip count
        context['trip_count'] = Trip.objects.all().count()
        # Calculate mileage
        context['mileage'] = Trip.objects.aggregate(mileage=Sum('odometer_close') - Sum('odometer_start'))
        # Calculate trip total collection
        context['trip_total_collection'] = Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum']
        return context

# class ExpenseListView(ListView):
#     model = Expense
#     template_name = 'realtrips/expense.html' # name of your  template
#     paginate_by=10

class TripAddView(LoginRequiredMixin, FormView):
    template_name = 'realtrips/addtrip.html'
    form_class = TripAddForm
    success_url = reverse_lazy('trips')

    def form_valid(self, form):
        profile = self.request.user.profile  # Assuming you have a 'Profile' model related to the user
        trip = form.save(commit=False)
        trip.profile = profile
        trip.save()

        # messages.success(self.request, 'Your Trip has been added. Thank you!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.form_class()
        messages.success(self.request, 'Your Trip has been added successfully. Thank you!')
        # return super().form_valid(form)
        return context

class EditVehicleView(LoginRequiredMixin,UpdateView):
    template_name = 'realtrips/update_vehicle.html'
    form_class = VehicleEditForm
    success_url = reverse_lazy('vehicle')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'Your Vehicle has been updated. Thank you!')
        return super().form_valid(form)

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Vehicle.objects.all()
    

class EditTripView(LoginRequiredMixin,UpdateView):
    template_name = 'realtrips/update_trip.html'
    form_class = EditTripForm
    success_url = reverse_lazy('trips')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'Your Trip has been updated. Thank you!')
        return super().form_valid(form)

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Trip.objects.all()
class VehicleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'realtrips/viewvehicle.html'
    success_url = reverse_lazy('viewvehicle')

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Vehicle.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # driver = Driver.objects.get(vehicle__vehicle_reg_no='vehicle_reg_no')
        # driver_name = driver.name
        # context['driver'] = driver
        return context
    

class TripDetailView(LoginRequiredMixin, DetailView):
    template_name = 'realtrips/viewtrip.html'
    success_url = reverse_lazy('viewtrip')

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Trip.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = self.get_object()
        # vehicle = trip.Vehicle
        expenses = Expense.objects.filter(Vehicle=trip.Vehicle, created=trip.created)
        # context['expenses'] = expenses
        return context

class RevenueListView(LoginRequiredMixin,ListView):
    template_name = 'realtrips/revenue_report.html'
    # template_name = 'realtrips/expense_report.html'
    success_url = reverse_lazy('trip')

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Expense.objects.filter(user='request.user.username')
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred
 
 
 # Calculate mileage for each trip
        trips = context['object_list']
        for trip in trips:
            trip.mileage = trip.odometer_close - trip.odometer_start
            context['trip.mileage']


        return context



    def total_amount_collected(self):
        return Trip.objects.aggregate(Sum('amount_collected'))['amount_collected_sum']

    def form_valid(self, form):
        form.save()

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Trip.objects.all()
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate the total amount collected
        total_amount_collected = Trip.objects.aggregate(Sum('amount_collected')).get('amount_collected__sum')
        context['total_amount_collected'] = total_amount_collected
            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred

         # Calculate the Net revenue
        net_revenue = total_amount_collected - total_expense_incurred
        context['net_revenue'] = net_revenue
        return context

# class ExpenseReportListView(LoginRequiredMixin, ListView):
#     template_name = 'realtrips/report-expense.html'
#     success_url = reverse_lazy('report-expense')

#     def get_queryset(self):
#         # Return a queryset of all Trip objects
#          return Expense.objects.filter(request.user)
#     # paginate_by=10

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#             # Calculate the total expenses
#         total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
#         context['total_expense_incurred'] = total_expense_incurred

#         return context

#     def get_queryset(self):
#         # Return a queryset of all Trip objects of current  logged in user
#          return Expense.objects.filter(request.user)
#          paginate_by=10

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#             # Calculate the total expenses
#         total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
#         context['total_expense_incurred'] = total_expense_incurred
#         return context
class ExpenseReportListView(LoginRequiredMixin, ListView):
    template_name = 'realtrips/report-expense.html'
    model = Expense
    context_object_name = 'expenses'
    paginate_by = 10 # display 10 items per page

    def get_queryset(self):
        # Return a queryset of all Expense objects of current logged in user
         return Expense.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred
        return context
    

from django.contrib.auth.mixins import LoginRequiredMixin

class ExpenseAddView(LoginRequiredMixin, FormView):
    template_name = 'realtrips/addexpense.html'
    form_class = ExpenseAddForm
    success_url = reverse_lazy('expense')

    def form_valid(self, form):
        profile = self.request.user.profile  # Assuming you have a 'Profile' model related to the user
        expense = form.save(commit=False)
        expense.profile = profile
        expense.save()

        # messages.success(self.request, 'Your Expense has been added. Thank you!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.form_class()
        messages.success(self.request, 'Your Expense has been added successfully. Thank you!')
        return context


class VehicleAddView(LoginRequiredMixin, FormView):
    template_name = 'realtrips/addvehicle.html'
    form_class = VehicleAddForm
    success_url = reverse_lazy('vehicle')

    def form_valid(self, form):
        profile = self.request.user  # Assuming you have a 'Profile' model related to the user
        vehicle = form.save(commit=False)
        vehicle.profile = profile
        vehicle.save()

        messages.success(self.request, 'Vehicle has been added. Thank you!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.form_class()
        messages.success(self.request, 'Vehicle  added successfully.')
        return context
    
class EditVehicleView(LoginRequiredMixin, UpdateView):
    form_class = VehicleEditForm
    template_name = 'realtrips/update_vehicle.html'
    success_url = reverse_lazy('vehicle')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, ' Vehicle details updated. Thank you!')
        return super().form_valid(form)

    def get_queryset(self):
        # Return a queryset of all Expense objects
        return Vehicle.objects.all()

class ExpenseDetailView(LoginRequiredMixin, DetailView):
    template_name = 'realtrips/viewexpense.html'
    success_url = reverse_lazy('trips')

    # def form_valid(self, form):
    #     form.save()

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Expense.objects.all()
        # return Expense.objects.filter(pk=expenser.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate total amount incurred
        total_expense_amount = Expense.objects.aggregate(Sum('amount_incurred'))['amount_incurred__sum']
        context['totalexpense_amount'] = total_expense_amount

        # total_trip_amount = Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum']
        # context['totaltrip_amount'] = total_trip_amount


        return context    

class EditExpenseView(LoginRequiredMixin, UpdateView):
    form_class = ExpenseEditForm
    template_name = 'realtrips/update_expense.html'
    success_url = reverse_lazy('expense')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your Expense  has been updated. Thank you!')
        return super().form_valid(form)

    def get_queryset(self):
        # Return a queryset of all Expense objects
        return Expense.objects.all()

class ExpenseDetailView(LoginRequiredMixin, DetailView):
    template_name = 'realtrips/viewexpense.html'
    success_url = reverse_lazy('trips')

    # def form_valid(self, form):
    #     form.save()

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Expense.objects.all()
        # return Expense.objects.filter(pk=expenser.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate total amount incurred
        total_expense_amount = Expense.objects.aggregate(Sum('amount_incurred'))['amount_incurred__sum']
        context['totalexpense_amount'] = total_expense_amount

        # total_trip_amount = Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum']
        # context['totaltrip_amount'] = total_trip_amount


        return context
