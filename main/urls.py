from django.urls import path 
from .views import *
# from . import views

urlpatterns = [
    #patterns for the url / , /products
    path('' , index , name="home"),
    path('detailed/<int:id>' , detailed_task , name ="detail"),
    path('todos/status/<str:st>' , todo_by_status , name ="status"),
    path('category/<int:id>/', category_todo, name='category_todos'),

    path('pending-todos/<str:st>', pending_todo, name='pending_todos'),
    path('inprogress-todos/<str:st>', inprogress_todo, name='inprogress_todos'),
    path('completed-todos/<str:st>', completed_todo, name='completed_todos'),

    path('todo/create' , Createtodo , name="createtodo"),
    path('categopry/create' , createCategory , name='createcategory' ),
    path('todo/update/<int:id>' , update_task , name ="update-task"),
    path('todo/delete/<int:id>' , delete_task , name ="delete-task"),



    path('signup/', SignUpView.as_view(), name='signup'),
]




