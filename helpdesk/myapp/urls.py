
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', views.Basepage, name='base'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.RegisterView, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name='password_reset_complete'),
    path('ChangePassword/', views.Change_Password, name='ChangePassword'),
    path('profile/', views.User_Profile, name='profile'),
    path('update_profile/<int:pk>', views.Update_Profile, name='update_profile'),
    path('taskdetails/', views.TaskDetails, name='taskdetails'),
    path('taskinfo/<int:pk>', views.TaskInfo, name='taskinfo'),
    path('update_task/<int:pk>', views.Update_Task, name='task_update'),
    path('delete_task/<int:pk>', views.Delete_Task, name='task_delete'),
    path('accept_task/<int:pk>', views.Accept_Task, name='task_accept'),
    path('remove_task/<int:pk>', views.RemoveTask, name='task_remove'),
    path('close_task/<int:pk>', views.CloseTask, name='task_close'),
    path('reopen_task/<int:pk>', views.Reopen_Task, name='task_reopen'),
    path('resolved_task/<int:pk>', views.Resolved_Task, name='task_resolved'),
    path('account', views.AccountDetails, name='account'),
    path('mycart', views.MyCarts, name='mycart'),

]
