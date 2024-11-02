from .models import *
from django.shortcuts import cr
from django.views.generic import UpdateView,DeleteView,CreateView,DetailView

class ShowListView(CreateView):
    model = Show
    template_name = "home.html"




class UpdateView(UpdateView):
    model = Order
    template_name = "home.html"



class  DeleteView(DeleteView):
    model = Order
    template_name = "home.html"
    

