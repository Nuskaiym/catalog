from django.contrib import admin
from django.urls import path, include

from product.views import *

urlpatterns = [
    path('sub/category/products/<int:sub_category_id>', CategoryProductsView.as_view(), name='sub_category_products'),
    path('manufacturer/products/<int:manufacturer_id>', ManufacturerProductsView.as_view(), name='manufacturer_products'),
    path('get/<int:product_id>', ProductView.as_view(), name='get_product'),
]
