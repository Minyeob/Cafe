from django.contrib import admin
from menu.models import Cafe, Coffee

class CoffeeInline(admin.TabularInline):
    model = Coffee
    extra = 2

class CafeAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Cafe information', {'fields': ['cafe_name', 'cafe_color']}),
                                 ]
    inlines = [CoffeeInline]            
    list_display = ('cafe_name', 'cafe_color')
    list_filter = ['cafe_color']
    search_fields = ['cafe_name']
                
admin.site.register(Cafe, CafeAdmin)
admin.site.register(Coffee)