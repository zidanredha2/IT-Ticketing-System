from django.db import models
from django.forms import forms
from django.contrib.auth.models import User
# Create your models here.

#UserProfile model
class UserProfile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    Address= models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State= models.CharField(max_length=100)

#TaskDetails Model
class TaskDetail(models.Model):
    TASK_TITLE = models.CharField(max_length=100)
    TASK_CREATED_BY = models.CharField(max_length=100, null=True)
    TASK_CLOSED_BY = models.CharField(max_length=100, null=True)
    TASK_CREATED_ON = models.DateField(auto_now_add=True,null=True)
    TASK_DUE_DATE = models.DateField()
    TASK_REWARD = models.IntegerField()
    TASK_CLOSED_ON = models.DateField(null=True)
    TASK_DESCRIPTION = models.CharField(max_length=300)
    TASK_HOLDER = models.CharField(max_length=100, null=True)
    choice=[('Open', 'Open'),('In-process', 'In-process'), ('Reopened', 'Reopened'), ('Closed', 'Closed'), ('Expired', 'Expired'), ('Resolved', 'Resolved')]
    TASK_STATUS = models.CharField(max_length=100,choices=choice, default='Open')
#MyCart Model
class MyCart(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    task= models.ForeignKey(TaskDetail, on_delete=models.CASCADE, null=True)
    task_count= models.IntegerField(default=1)

#Account Model
class Account(models.Model):
    ACCOUNT_HOLDER = models.OneToOneField(User,  on_delete=models.CASCADE, null=True)
    ACCOUNT_BALANCE= models.IntegerField()

