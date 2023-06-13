from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import User
from django.views import generic 
from django.template import loader


class home_page(generic.ListView):
    template_name = 'files/homehtml.html'
    context_object_name = 'Main_page'

    def get_queryset(self):
        
        return User.objects.order_by('-id')



    

    

