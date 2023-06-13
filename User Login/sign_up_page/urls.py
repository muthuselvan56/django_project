from django.urls import path, include
from . import views


app_name= 'sign_up_page'

urlpatterns = [
    path('',views.sign_form.as_view(),name='formal'),
    path('regi_form',views.register_form,name='regi')

]