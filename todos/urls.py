from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='todos_home'),
    path('add/', views.add_todo, name='add_todo'),
    path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
