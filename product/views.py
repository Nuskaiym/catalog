from django.shortcuts import render
from django.views.generic import TemplateView

from product.models import *


class CategoryProductsView(TemplateView):
    template_name = 'category/listProduct.html'

    def get(self, request, *args, **kwargs):
        sub_category = SubCategory.objects.get(id=kwargs['sub_category_id'])
        products = Product.objects.order_by('-id').filter(sub_category=sub_category)
        return render(request, self.template_name, context={
            'products': products,
            'sub_category': sub_category,
        })


class ManufacturerProductsView(TemplateView):
    template_name = 'category/listManufacturerProduct.html'

    def get(self, request, *args, **kwargs):
        manufacturer = Manufacturer.objects.get(id=kwargs['manufacturer_id'])
        products = Product.objects.order_by('-id').filter(manufacturer=manufacturer)
        return render(request, self.template_name, context={
            'products': products,
            'manufacturer': manufacturer,
        })
