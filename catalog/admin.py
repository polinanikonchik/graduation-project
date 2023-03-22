from django.contrib import admin
from .models import Product, Manufacturer, Country, Category


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'category', 'country', 'price', 'image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

# admin.site.register(Country)
