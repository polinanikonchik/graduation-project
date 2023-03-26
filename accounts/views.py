from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from cart.models import Cart

from .forms import UserRegistrationForm


class Registration(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Cart.objects.create(user=new_user)
            return redirect('catalog-index')
        return render(request, self.template_name, {'user_form': user_form})
