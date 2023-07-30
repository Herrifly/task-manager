from django.shortcuts import render, get_object_or_404
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
    if request.method == 'GET':
        button_pressed = request.GET.get('button', '')

        if button_pressed == 'in progress':
            tasks = Task.objects.filter(status='In progress').order_by('deadline')
        elif button_pressed == 'awaiting':
            tasks = Task.objects.filter(status='Awaiting').order_by('deadline')
        elif button_pressed == 'completed':
            tasks = Task.objects.filter(status='Completed').order_by('deadline')
        elif button_pressed == 'all':
            tasks = Task.objects.all().order_by('deadline')
        else:
            tasks = Task.objects.all().order_by('deadline')

    all_tasks = []

    for task in tasks:
        task_info = {
            'name': task.name,
            'description': task.description,
            'deadline': task.deadline,
            'priority': task.priority,
            'status': task.status,
            'id': task.id
        }
        all_tasks.append(task_info)

    context = {'all_info': all_tasks}
    return render(request, 'task-manager-app/tasks.html', context)


def delete(request, id):
    data = get_object_or_404(Task, id=id)
    data.delete()
    return tasks(request)