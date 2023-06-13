from django.urls import path, include
from . import views
from sign_up_page.views import signup_form
from log_in.views import texter


app_name= 'sign_up'
urlpatterns = [
      path('',views.home_page.as_view(),name='home'),
      path('signed/',signup_form,name='singed'),
      path('log_ed/',texter,name='loge_d'),   
        
]