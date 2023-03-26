from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    Category,
    Country,
    Manufacturer,
    Product,
)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'category', 'country', 'price', 'image')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview')
    readonly_fields = ('get_image',)

    def preview(self, obj):
        if not obj.image:
            return None
        return mark_safe(
            f'<img src="{obj.image.url}" style="height: 70px; width: 70px; object-fit: cover;">')

    preview.short_description = 'изображение'

    def get_image(self, obj):
        if not obj.image:
            return None
        return mark_safe(f'<img src="{obj.image.url}" style="height: 250px;">')

    get_image.short_description = 'изображение'
