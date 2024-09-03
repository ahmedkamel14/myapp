from django.shortcuts import render , get_object_or_404 , redirect

#return http response 
from django.http import HttpResponse
#IMPORT MODELS
from .models import Task , Category 

from .forms import TaskForm , CategoryForm

from django.contrib.auth.decorators import login_required


# signup

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth import login as auth_login

#  Create your views here.

#   Function base view 

@login_required
def index(request):
    #SELECT * from Task ;
    # tasks = Task.objects.all().order_by('due_date')
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    categories = Category.objects.filter(user=request.user)

    context = { 'tasks':tasks ,
                'categories' :categories
              }
    # return HttpResponse(tasks)
    return render(request , 'main/index.html',context)

@login_required
def detailed_task(request ,id):
    task = Task.objects.get(id=id)
    context = {
        'task':task
    }
    return render(request , 'main/detailed.html' , context)
#Class Base View 



@login_required
def todo_by_status(request , st):
    todos = Task.objects.filter(status = st)
    context = {
        'todos' :todos
    }
    return render(request , 'main/todosstatus.html' , context)

@login_required
def category_todo(request, id):
    category = Category.objects.get(id=id)
    todos = Task.objects.filter(category=category)
    context = {
        'category': category,
        'todos': todos
    }
    return render(request, 'main/category_todos.html', context)

@login_required
def pending_todo(request, st):
    pending_todos = Task.objects.filter(status = st)
    return render(request, 'main/pending_todos.html', {'pending_todos': pending_todos})
@login_required
def inprogress_todo(request, st):
    inprogress_todos = Task.objects.filter(status = st)
    return render(request, 'main/inprogress.html', {'inprogress_todos': inprogress_todos})

@login_required
def completed_todo(request, st):
    completed_todos = Task.objects.filter(status = st)
    return render(request, 'main/completed_todos.html', {'completed_todos': completed_todos})



@login_required
#create task 
def Createtodo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid() :
            task=form.save(commit=False) #--> save the record in database
            task.user=request.user
            task.save()            
            return redirect('home')
    else:  
        form = TaskForm()
    return render(request , 'main/create_todo.html' ,{'form' :form} )


@login_required
def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid() :
            cat=form.save(commit=False) #--> save the record in database
            cat.user=request.user
            cat.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = CategoryForm()
    return render(request , 'main/createCategorys.html' ,{'form':form})


@login_required
def update_task(request , id ):
    task = get_object_or_404(Task , id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid() :
            form.save() #--> save the record in database            
            return redirect('home')
    else:  
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html' , {'form':form})
@login_required
def delete_task(request , id):
    task = get_object_or_404(Task , id=id)
    task.delete()
    return redirect('home')








class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'






# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('index') 
#     else:
#         form = UserCreationForm()
#     return render(request, 'main/signup.html', {'form': form})


