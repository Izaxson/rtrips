from django import views
from django.urls import include, path

from accounts.views import LoginView


# from Vehicles import settings
from .views import   EditTripView, EditVehicleView, ExpenseAddView,ExpenseReportListView,RevenueListView,EditExpenseView,ExpenseDetailView, TripDetailView, TripAddView, TripListView , ExpenseListView , DashboardView, VehicleAddView, VehicleDetailView, VehicleListView
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [

    #dashboard 
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #Trips
    path('trips/', TripListView.as_view(), name='trips'),
    path('addtrip/', TripAddView.as_view(), name='addtrip'),
    path('edittrip/<str:pk>', EditTripView.as_view(), name='edit-trip'),
    path('viewtrip/<str:pk>', TripDetailView.as_view(), name='viewtrip'),
    #Reports
    path('report-trip/', RevenueListView.as_view(), name='revenue_report'),
    path('report-expense/', ExpenseReportListView.as_view(), name='report-expense'),
    # path("tripfilter/", FilterTripView.as_view(model=Trip), name="trip"),
    #Expenses
    path('expense/', ExpenseListView.as_view(), name='expense'),
    path('addexpense/', ExpenseAddView.as_view(), name='addexpense'),
    path('editexpense/<str:pk>',EditExpenseView.as_view(), name='edit-expense'),
    path('viewexpense/<str:pk>',ExpenseDetailView.as_view(), name='viewexpense'),
    #Vehicle 
    path('vehicle/', VehicleListView.as_view(), name='vehicle'),
    path('addvehicle/', VehicleAddView.as_view(), name='addvehicle'),
    path('editvehicle/<str:pk>', EditVehicleView.as_view(), name='edit-vehicle'),
    path('viewvehicle/<str:pk>', VehicleDetailView.as_view(), name='view-vehicle'),
 ]
