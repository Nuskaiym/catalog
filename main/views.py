from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomeViews(TemplateView):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
