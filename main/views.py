from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Product


# Create your views here.

class HomeViews(TemplateView):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        top_products = Product.objects.all().filter(is_top=True)[:6]
        new_products = Product.objects.all().filter(is_new=True)[:3]

        return render(request, self.template_name, {
            'top_products': top_products,
            'new_products': new_products
        })
