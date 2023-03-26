from django.shortcuts import render
from django.views.generic import TemplateView
from cart.cart import get_cart
from .models import *


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        products = Product.objects.all()
        params = {
            'products': products,
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = 'catalog/index.html'

    def post(self, request):
        content = request.POST['content']
        products_by_title = Product.objects.filter(title__icontains=content)
        products_by_summary = Product.objects.filter(summary__icontains=content)
        result = products_by_title.union(products_by_summary, all=False)
        params = {
            'products': result
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class Registration(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request):
        return render(request, self.template_name)


class ManufacturersView(TemplateView):
    template_name = 'catalog/manufacturers.html'

    def get(self, request):
        manufacturers = Manufacturer.objects.all()
        params = {
            'manufacturers': manufacturers
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class CountriesView(TemplateView):
    template_name = 'catalog/countries.html'

    def get(self, request):
        countries = Country.objects.all()
        params = {
            'countries': countries,
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class CategoriesView(TemplateView):
    template_name = 'catalog/categories.html'

    def get(self, request):
        categories = Category.objects.all()
        params = {
            'categories': categories
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class ManufacturerView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        manufacturer = Manufacturer.objects.all()
        params = {
            'manufacturer': manufacturer
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class CategoryView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, name):
        country = Country.objects.get(name=name)
        products = Product.objects.filter().all()
        params = {
            'country': country,
            'products': products
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class CountryView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request):
        country = Country.objects.all()
        params = {
            'country': country
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class ProductsView(TemplateView):
    template_name = 'catalog/products.html'

    def get(self, request, id):
        products = Product.objects.get(id=id)
        params = {
            'products': products
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)


class ProductView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, id):
        product = Product.objects.get(id=id)
        params = {
            'product': product
        }
        params = get_cart(request, params)
        return render(request, self.template_name, params)
