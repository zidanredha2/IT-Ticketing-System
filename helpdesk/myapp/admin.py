from django.contrib import admin
from .models import UserProfile, TaskDetail, MyCart, Account
# Register your models here.
#UserProfile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['Address', 'City', 'State']
admin.site.register(UserProfile, UserProfileAdmin)

#TaskDetails Admin
class TaskDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'TASK_TITLE','TASK_DEPARTMENT', 'TASK_CREATED', 'TASK_CLOSED', 'TASK_CREATED_ON', 'TASK_DUE_DATE', 'TASK_REWARD', 'TASK_CLOSED_ON', 'TASK_DESCRIPTION', 'TASK_HOLDER', 'TASK_STATUS']
admin.site.register(TaskDetail, TaskDetailsAdmin)
#MyCart Admin
class MyCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'task', 'task_count']
admin.site.register(MyCart, MyCartAdmin)
#Account Admin
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id','ACCOUNT_HOLDER', 'ACCOUNT_BALANCE']
admin.site.register(Account, AccountAdmin)
