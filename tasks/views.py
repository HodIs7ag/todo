from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def index(request):
	tasks = Task.objects.all()
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			task = form.cleaned_data.get('title')
			messages.success(request,f"{task}")
			return redirect("/")
	context = {
		'tasks':tasks,
		'form':form
	}
	return render(request,'tasks/list.html',context)

def updateTask(request,pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('tasks:list')
	context = {
		'form':form
	}
	return render(request,"tasks/update.html",context)


def deleteTask(request,pk):
	task = Task.objects.get(id=pk)
	task.delete()
	return redirect('tasks:list')

