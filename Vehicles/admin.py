from django.contrib import admin

from Vehicles.models import Expense, Route, Trip, Vehicle
class TripAdmin(admin.ModelAdmin):
    list_display = ('Vehicle','odometer_start', 'odometer_close', 'journey_start','journey_destination','amount_collected')
    list_filter = ("Vehicle",)
    list_filter = ("journey_start",)

class RouteAdmin(admin.ModelAdmin):
    list_display = ('Vehicle', 'route', 'created')
    list_filter = ("Vehicle",)
   

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('Vehicle', 'name', 'amount_incurred','created','updated')
    list_filter = ("Vehicle","name","amount_incurred","created")

    search_fields = ['Vehicle']    


admin.site.register(Vehicle)
admin.site.register(Trip, TripAdmin)
admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Route, RouteAdmin)