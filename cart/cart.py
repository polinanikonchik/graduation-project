from .models import Cart


def get_cart(request, params):
    try:
        cart = Cart.objects.filter(user=request.user).first()
        params['cart'] = cart
    except:
        pass
    finally:
        return params
