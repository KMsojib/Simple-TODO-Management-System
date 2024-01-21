from django.contrib import admin

# Register your models here.
from Todo.models import TaskModel 

class ToDoModelAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription', 'is_completed')


admin.site.register(TaskModel,ToDoModelAdmin)