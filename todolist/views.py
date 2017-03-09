from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos,
        'title': 'Todolist',
    }
    return render(request, 'index.html', context)

def details(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
        'title': todo.title
    }
    return render(request, 'details.html', context)

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/')
    else:
        return render(request, 'add.html')
