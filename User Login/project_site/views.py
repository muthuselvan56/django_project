from django.shortcuts import render, redirect
from sign_up.models import User
from django.http import HttpResponse
from django.views import generic 
from django.template import loader


def request_redirect(request):
    return redirect('/main_page')

def log_out(request):

  template = loader.get_template('files/go_back.html')
  return HttpResponse(template.render())    
    


    

