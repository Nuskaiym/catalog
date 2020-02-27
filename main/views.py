from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Product

from message.forms import MessageForm


# Create your views here.

class HomeViews(TemplateView):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        top_products = Product.objects.all().filter(is_top=True)[:6]
        new_products = Product.objects.all().filter(is_new=True)[:3]
        return render(request, self.template_name, {
            'top_products': top_products,
            'new_products': new_products,
        })

    # def post(self, request, *args, **kwargs):
    #     message_form = MessageForm(data=request.POST)
    #     if message_form.is_valid():
    #         print('postko keldi')
    #         new_message = message_form.save(commit=False)
    #         new_message.save()
    #         return HttpResponseRedirect('/')
    #     else:
    #         print('no valid!!!!!!!!!!!')
    #     return HttpResponse('invalid form')


def send_message(request, *args, **kwargs):
    message_form = MessageForm(data=request.POST)
    if message_form.is_valid():
        print('postko keldi')
        new_message = message_form.save(commit=False)
        new_message.save()
        return HttpResponseRedirect('/')
    else:
        print('no valid!!!!!!!!!!!')
    return HttpResponse('invalid form')
