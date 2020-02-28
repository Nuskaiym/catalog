from message.forms import MessageForm
from product.models import *
from main.models import *
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


@register.inclusion_tag('main/contact_form.html')
def contact_tag():
    message_form = MessageForm()
    return {'message_form': message_form}


@register.inclusion_tag('category/list_manufacturer.html')
def manufacturer_tag():
    manufacturers = Manufacturer.objects.all()
    return {'manufacturers': manufacturers}


@register.inclusion_tag('main/slider.html')
def slider():
    slider = Slider.objects.all()
    return {'slider': slider}
