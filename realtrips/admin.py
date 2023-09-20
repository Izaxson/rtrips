from django.contrib import admin

from realtrips.models import Company, Driver, Expense, Profile, Route,   Trip, Vehicle
class TripAdmin(admin.ModelAdmin):
    list_display = ('Vehicle','odometer_start', 'odometer_close', 
                    'journey_start','journey_destination','amount_collected','profile')
    list_filter = ("Vehicle"),
    
class DriverAdmin(admin.ModelAdmin):
    # list_filter = ("Vehicle",'name'),
    search_fields = ['vehicle']
   

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('Vehicle', 'name', 'amount_incurred','created','profile')
    list_filter = ("Vehicle","name","amount_incurred","created","profile")
    
    # search_fields = ['Vehicle']    


admin.site.register(Vehicle)
admin.site.register(Trip, TripAdmin)
admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Route)
admin.site.register(Profile)
admin.site.register(Driver,DriverAdmin)
admin.site.register(Company)