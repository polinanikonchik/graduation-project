from __future__ import annotations

from typing import Union

from django.db import models
from django.db.models import Manager
from django.urls import reverse

try:
    from cart.models import Cart
except ImportError:
    ...


class Country(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="countries/",
        blank=True,
        default="image-placeholder.jpeg",
    )

    def __str__(self):
        return self.name

    def get_country_url(self):
        return reverse('catalog-country', args=[self.name])


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to="manufacturers/",
        blank=True,
        default="photo-placeholder.jpeg",
    )

    def __str__(self):
        return f"{self.id}"

    def get_manufacturer_url(self):
        return reverse('catalog-manufacturer', args=[self.id])


class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to="categories/",
        blank=True,
        default="category-placeholder.jpeg",
    )

    def __str__(self):
        return self.name

    def get_country_url(self):
        return reverse('catalog-category', args=[self.name])


class Product(models.Model):
    title = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    image = models.ImageField(
        upload_to="product/",
        blank=True,
        default="product-placeholder.jpeg",
    )
    cart: Union[Cart, Manager]

    def __str__(self):
        return f'{self.title}'

    def display_country(self):
        return ', '.join([country.name for country in self.country.all()])

    def get_product_url(self):
        return reverse('catalog-product', args=[self.id])

    def add_to_cart(self):
        return reverse('cart-add', args=[self.id])

    display_country.short_description = 'Country'
