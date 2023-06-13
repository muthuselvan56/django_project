from django.urls import path, include
from . import views


app_name= 'log_in'
urlpatterns = [
     path('',views.login_form.as_view(),name='logger'),
     path('login',views.login,name='index'),
     path('logout',views.logout,name='log')
]