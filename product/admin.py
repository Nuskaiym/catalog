from django.contrib import admin

from product.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    search_fields = ['title']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'is_active']
    search_fields = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'sub_category', 'manufacturer']
    # list_display_links = None
    search_fields = ['title', 'text']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
