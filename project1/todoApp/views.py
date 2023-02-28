from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import ToDoForm
from django.views.generic import ListView, UpdateView,DeleteView
from  django.views.generic.detail import DetailView

# Create your views here.

def home(request):
    task2 = task.objects.all
    if request.method == 'POST':
        name = request.POST.get('name', "")
        priority = request.POST.get('priority', "")
        date = request.POST.get('date', "")
        task1 = task(name=name, priority=priority, date = date)
        task1.save()
        return redirect('/')
    return render(request, 'home.html', {'task': task2})


def delete(request, taskid):
    task1 = task.objects.get(id=taskid)
    if request.method == 'POST':
        task1.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id1):
    task1 = task.objects.get(id=id1)
    f = ToDoForm(request.POST or None, instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task1':task1})


class listView(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task'



class taskDetail(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'


class taskUpdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk': self.object.id})


class taskDelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

