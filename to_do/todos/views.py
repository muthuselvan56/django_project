from django.template import loader 
from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponseRedirect  , HttpResponse
from django.views import generic 
from .models import Todo

# Create your views here.

# def show(request):
#     variable = loader.get_template('todos/index.html')
#     return HttpResponse(variable.render())

class show_todos(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        
        return Todo.objects.order_by('-created_at')
def add(request):
    # sending multiplay perameter to model
    
    title = request.POST['task_name']
    Todo.objects.create(title=title)
    return redirect('todos:index') 



def delete(request,todo_id):
    todo = get_object_or_404(Todo,pk=todo_id)
    todo.delete()
    return redirect('todos:index')

def update(request,todo_id):
    todo = get_object_or_404(Todo,pk=todo_id)
    print(todo_id)
    print(todo)
    iscompleted= request.POST.get('isCompleted',False)
    if iscompleted == 'on':
        iscompleted = True
        
    todo.isCompleted = iscompleted  
    todo.save()
    return redirect('todos:index')  