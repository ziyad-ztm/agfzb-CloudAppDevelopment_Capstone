from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel


# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'dealer_id', 'type', 'year']

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)