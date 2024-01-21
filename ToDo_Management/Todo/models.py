from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField(max_length=1000)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.taskTitle

    