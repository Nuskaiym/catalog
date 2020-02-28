from django.contrib import admin
from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('/send/message', send_message, name='send_message'),
]
