from django.shortcuts import render
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()

    form = TaskForm()

    context = {'form': form}
    return render(request, 'task-manager-app/index.html', context)


def tasks(request):
    tasks = Task.objects.order_by('deadline')
    all_tasks = []
    id = 1
    for task in tasks:
        task_info = {
            'name': task.name,
            'description': task.description,
            'deadline': task.deadline,
            'priority': task.priority,
            'status': task.status,
            'id': 1
        }
        id += 1
        all_tasks.append(task_info)

    context = {'all_info': all_tasks}
    return render(request, 'task-manager-app/tasks.html', context)
