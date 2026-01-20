from django.contrib import admin
from .models import User, CarModel, Part

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('oem_code', 'name', 'category', 'price')
    search_fields = ('oem_code', 'name')
    list_filter = ('category', 'compatible_with')

admin.site.register(User)
admin.site.register(CarModel)
