from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return HttpResponse('<br>'.join([task.title for task in tasks]))
