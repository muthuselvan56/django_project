
from django.contrib import admin
from django.urls import path, include
from . import views , settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.request_redirect),
    path('main_page/',include('sign_up.urls')),
    path('register/',include('sign_up_page.urls')),
    path('logg/',include('log_in.urls')),
    path('logout/',views.log_out),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
