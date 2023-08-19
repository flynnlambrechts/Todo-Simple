from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    code = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
    
    class Meta:
        ordering = ['create']

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']