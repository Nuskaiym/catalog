from django.contrib import admin
from django.urls import path, include

from main.views import HomeViews

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
]
