# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from django.contrib import admin
from .models import CarMake, CarModel

# Customizing the admin display for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'country']

# Customizing the admin display for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_type', 'year', 'make', 'dealer_id']
    list_filter = ['car_type', 'year', 'make']
    search_fields = ['name', 'make__name']

# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)