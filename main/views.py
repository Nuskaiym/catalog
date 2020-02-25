from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from message.forms import MessageForm


class HomeViews(TemplateView):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        message_form = MessageForm()
        return render(request, self.template_name, {
            'message_form': message_form,
        })

    def post(self, request, *args, **kwargs):
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            print('postko keldi')
            new_message = message_form.save(commit=False)
            new_message.save()
            return HttpResponseRedirect('/')
        else:
            print('no valid!!!!!!!!!!!')
        return HttpResponse('invalid form')