from .views import *
from django.urls import path

urlpatterns = [
    path('', Order.as_view(), name='home'),
    path('', Movie.as_view(), name='home'),
    path('', Category.as_view(), name='home'),
    path('', Show.as_view(), name='home')

]
