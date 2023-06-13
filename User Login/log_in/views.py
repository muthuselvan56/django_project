from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import generic 
from sign_up.models import User

def texter(request):
    return redirect('/logg')

class login_form(generic.ListView):
        template_name = 'files/login.html'
        context_object_name = 'sign_page'

        def get_queryset(self):     
           return User.objects.order_by('-id')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()

        if user:
            return redirect('/logout/')
            
        else:
            
            return redirect('/logg/') 

            
    return render(request, 'files/login.html')        

def logout(request):

    return redirect('/main_page/')


# Create your views here.
