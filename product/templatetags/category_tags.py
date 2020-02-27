from product.models import *
from django import template

register = template.Library()


@register.inclusion_tag('category/listCategory.html')
def categories_tag():
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('category/modal_footer.html')
def modal_categories_tag():
    categories = Category.objects.all()
    return {'categories': categories}
