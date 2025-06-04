from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import LoginForm, RegisterForm, UserProfileForm, TaskDetailForm, AccountForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile, TaskDetail, MyCart, Account
# Create your views here.
def Basepage(request):
    if request.user.is_authenticated:
        Taskdatas= TaskDetail.objects.all()
        return render(request, 'Base.html', {'Taskdatas': Taskdatas})
    else:
        messages.success(request, 'Please login to view your profile')
        return redirect('login')
    
    return render(request, 'Base.html')
#LoginView
def LoginView(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Login successful')
                return redirect('base')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'Login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'Login.html', {'form': form})
#LogoutView
def LogoutView(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('login')
#RegisterView
def RegisterView(request):
    if request.method == 'POST':
        Register_form = RegisterForm(request.POST)
        UserProfile_form = UserProfileForm(request.POST)
        if Register_form.is_valid() and UserProfile_form.is_valid():
            Registerform= Register_form.save()
            UserProfileform= UserProfile_form.save(commit=False)
            Address = UserProfile_form.cleaned_data['Address']
            City = UserProfile_form.cleaned_data['City']
            State = UserProfile_form.cleaned_data['State']
            profile = UserProfile(user=Registerform, Address=Address, City=City, State=State)
            profile.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please try again.')
            return redirect('register')
    else:
        Register_form = RegisterForm()
        UserProfile_form = UserProfileForm()
        return render(request, 'Register.html', {'Register_form': Register_form, 'UserProfile_form': UserProfile_form})
    #Change_Password
def Change_Password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'Password changed successfully')
            return redirect('login')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'Change_Password.html', {'fm': fm})

#User_Profile
def User_Profile(request):
    if request.user.is_authenticated:
        user= request.user
        ProfileDatas = UserProfile.objects.filter(user=user)
        AccountDatas = Account.objects.filter(ACCOUNT_HOLDER=user)
        return render(request, 'Userprofile.html', {'AccountDatas': AccountDatas, 'ProfileDatas': ProfileDatas})
    else:
        messages.success(request, 'Please login to view your profile')
        return redirect('login')
# Update_Profile
def Update_Profile(request, pk):
    if request.user.is_authenticated:
        ProfileDatas= UserProfile.objects.get(id=pk)
        form = UserProfileForm(request.POST or None, instance=ProfileDatas)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        return render(request, 'Update_Profile.html', {'form': form})
    else:
        messages.success(request, 'Please login to view your profile')
        return redirect('login')
#Task Creation Function
def TaskDetails(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = TaskDetailForm(request.POST)
            if form.is_valid():
                Task=form.save(commit=False)
                Task.TASK_CREATED = request.user
                Task.save()
                messages.success(request, 'Task created successfully')
            return redirect('base')
        else:
            form = TaskDetailForm()
            return render(request, 'TaskDetail.html', {'form': form})
    else:
        messages.success(request, 'Please login to create a task')
        return redirect('login')
#TaskInfo
def TaskInfo(request, pk):
    if request.user.is_authenticated:
        taskinfos= TaskDetail.objects.get(id=pk)
        return render(request, 'TaskInfo.html', {'taskinfos': taskinfos})
    else:
        messages.success(request, 'Please login to view task details')
        return redirect('login')
#UpdateTask
def Update_Task(request, pk):
    if request.user.is_authenticated:
        taskinfos=TaskDetail.objects.get(id=pk)
        form = TaskDetailForm(request.POST or None, instance=taskinfos)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully')
            return redirect('base')
        return render(request, 'Update_Task.html', {'form': form})
    else:
        messages.success(request, 'Please login to view tasks.')
        return redirect('login')
#DeleteTask
def Delete_Task(request, pk):
    if request.user.is_authenticated:
        taskinfos= TaskDetail.objects.get(id=pk)
        taskinfos.delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('base')
    else:
        messages.success(request, 'Please login to delete tasks.')
        return redirect('login')
#AcceptTask
def Accept_Task(request, pk):
    if request.user.is_authenticated:
        currentuser = request.user
        taskinfos= TaskDetail.objects.get(id=pk)
        taskinfos.TASK_STATUS = 'In-process'
        taskinfos.save()
        MyCart(user=currentuser, task=taskinfos).save()
        messages.success(request, 'Task accepted successfully')
        return redirect('mycart')
    else:
        messages.success(request, 'Please login to accept tasks.')
        return redirect('login')
#MyCart
def MyCarts(request):
    if request.user.is_authenticated:
        currentuser = request.user
        Carts= MyCart.objects.filter(user=currentuser)
        return render(request, 'MyCart.html', {'Carts': Carts})
    else:
        messages.success(request, 'Please login to View your tasks.')
        return redirect('login')
# Remove Task
def RemoveTask(request, pk):
    if request.user.is_authenticated:
        Taskdatas= TaskDetail.objects.get(id=pk)
        Taskdatas.TASK_STATUS= 'Open'
        Taskdatas.save()
        mycart = MyCart.objects.filter(task=pk)
        mycart.delete()
        messages.success(request, 'Task removed successfully')
        return redirect('mycart')
    else:
        messages.success(request, 'Please login to remove tasks.')
        return redirect('login')
# Closed Task
def CloseTask(request, pk):
    if request.user.is_authenticated:
        Taskdatas= TaskDetail.objects.get(id=pk)
        Taskdatas.TASK_STATUS= 'Closed'
        Taskdatas.TASK_CLOSED = request.user
        Taskdatas.TASK_CLOSED_ON = timezone.now()
        Taskdatas.save()
        mycart = MyCart.objects.filter(task=pk)
        mycart.delete()
        messages.success(request, 'Task closed successfully')
        return redirect('mycart')
    else:
        messages.success(request, 'Please login to close tasks.')
        return redirect('login')
#ReopenTask
def Reopen_Task(request, pk):
    if request.user.is_authenticated:
        currentuser = request.user
        taskinfos= TaskDetail.objects.get(id=pk)
        taskinfos.TASK_STATUS = 'Reopened'
        holder = User.objects.get(username=taskinfos.TASK_CLOSED)
        taskinfos.save()
        MyCart(user=holder, task=taskinfos).save()
        messages.success(request, 'Task opened successfully')
        return redirect('base')
    else:
        messages.success(request, 'Please login to open tasks.')
        return redirect('login')
#ResolvedTask
def Resolved_Task(request, pk):
    if request.user.is_authenticated:
        taskinfos= TaskDetail.objects.get(id=pk)
        taskinfos.TASK_STATUS = 'Resolved'
        #holder = User.objects.get(username=taskinfos.TASK_CLOSED)
        taskinfos.save()
        messages.success(request, 'Task resolved successfully')
        return redirect('base')
    else:
        messages.success(request, 'Please login to resolve tasks.')
        return redirect('login')
#Account Function
def AccountDetails(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                Task=form.save(commit=False)
                Task.TASK_CREATED = request.user
                Task.save()
                messages.success(request, 'Coins added successfully!')
            return redirect('base')
        else:
            form = AccountForm()
            return render(request, 'Account.html', {'form': form})
    else:
        messages.success(request, 'Please login to add coins.')
        return redirect('login')
