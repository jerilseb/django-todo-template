from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from todos.models import Todo
from todos.forms import TodoForm

@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()
    context = {'todos': todos, 'form': form}
    return render(request, 'todos.html', context)

@require_POST
@login_required
def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
    return redirect('index')

@login_required
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('index')
