from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from todolist.models import Todo


def index(request):
    context = {}
    if request.user.is_authenticated:
        # Give the list todo todos
        todos = Todo.objects.filter(user=request.user.id)
        context['todos'] = todos

    return render(request, 'todolist/index.html', context)

def add_todo(request):
    if request.method != 'POST':
        context = {'error_message' : 'Invalid HTTP request'}
        render(request, 'todolist/index.html', context)

    try:
        todo = request.POST['todo']
    except KeyError:
        context = {'error_message' : 'Todo is not Found'}
        return render(request, 'todolist/index.html', context)
    
    if todo == '':
        return HttpResponseRedirect(reverse('todolist:index'))

    # Add todo
    todo = Todo(user=request.user, text=todo)
    todo.save()

    return HttpResponseRedirect(reverse('todolist:index'))

def delete_todo(request, todo_id):
    if request.method != 'POST':
        context = {'error_message' : 'Invalid HTTP request'}
        render(request, 'todolist/index.html', context)

    # Find the todo from DB
    todo = get_object_or_404(Todo, pk=todo_id)

    # Delete from DB
    todo.delete()

    # Redirect to index
    return HttpResponseRedirect(reverse('todolist:index'))
