from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('add_tasks/', views.add_tasks, name='add_tasks'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:id>/', views.complete_task, name='complete_task'),
    path('delete_completed_task/<int:id>/', views.delete_completed_task, name='delete_completed_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
]
