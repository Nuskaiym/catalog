from django.contrib import admin
from main.models import Slider


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


admin.site.register(Slider, SliderAdmin)
