from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# List all tasks
def todoactions(request):
    todos = Todo.objects.all()
    return render(request, 'todoactions/todo_list.html', {'todos': todos})

# Create a new task
def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
        return redirect('todoactions')
    return render(request, 'todoactions/create_todo.html')

# Update a task
def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todoactions')
    return render(request, 'todoactions/update_todo.html', {'todo': todo})

# Delete a task
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todoactions')
    return render(request, 'todoactions/delete_todo.html', {'todo': todo})
