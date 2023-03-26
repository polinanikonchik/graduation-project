from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from catalog.models import Product

from .models import Cart


class CartView(TemplateView):
    @method_decorator(login_required())
    def get(self, request, id):
        product = Product.objects.get(id=id)
        cart = Cart.objects.get(user=request.user)
        cart.products.add(product)

        return redirect('catalog-index')
