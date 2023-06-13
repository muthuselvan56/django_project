# create a urls path here

from django.urls import path , include
from . import views

app_name = 'todos'
urlpatterns = [
    # path('',views.show),
    path('',views.show_todos.as_view(),name='index'),
    path('<int:todo_id>/delete',views.delete,name='delete'),
    path('<int:todo_id>/update',views.update,name='update'),
    path('add/',views.add,name='add'),

]
