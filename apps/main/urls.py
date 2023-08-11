from django.urls import path
from .views import list_todos,create_todos,delete_todos,update_todo
urlpatterns =[
    path('',list_todos),#http://127.0.0.1:8000/todos/
    path('create/',create_todos),#http://127.0.0.1:8000/todos/create/
    path('delete/<int:pk>/',delete_todos),#http://127.0.0.1:8000/todos/delete/int/
    path('update1/<primary_key>/',update_todo)#http://127.0.0.1:8000/todos/update1/
]