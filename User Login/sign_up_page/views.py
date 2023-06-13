from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from sign_up.models import User
from django.shortcuts import redirect , render
from django.views import generic 



def signup_form(request):
        return redirect('/register')

class sign_form(generic.ListView):
        template_name = 'files/signup.html'
        context_object_name = 'sign_page'

        def get_queryset(self):     
           return User.objects.order_by('-id')
        
def register_form(request):
       
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create(username=username, password=password, email=email)
        return redirect('/main_page')
    
    return render(request, 'signup.html')







