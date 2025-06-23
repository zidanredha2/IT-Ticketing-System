
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import UserProfile, TaskDetail, Account
#LoginForm
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
# RegisterForm
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

# UserProfileForm
class UserProfileForm(forms.ModelForm):
    Address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    City = forms.CharField(label='City', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    State = forms.CharField(label='State', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = UserProfile
        fields = ( 'Address','City', 'State')
#TaskDetail Form
class TaskDetailForm(forms.ModelForm):
    TASK_TITLE = forms.CharField(label='Ticket Title', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    TASK_DEPARTMENT = forms.ModelChoiceField(label='Concerned Department', queryset=Group.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    TASK_DUE_DATE = forms.DateField(label= 'Ticket Due Date', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}))
    TASK_REWARD = forms.IntegerField(label= 'Ticket Reward')
    TASK_DESCRIPTION = forms.CharField(label='Ticket Description', max_length=300, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= TaskDetail
        fields = ('TASK_TITLE','TASK_DEPARTMENT', 'TASK_DUE_DATE', 'TASK_REWARD', 'TASK_DESCRIPTION',)
# AccountForm
class AccountForm(forms.ModelForm):
    ACCOUNT_HOLDER = forms.ModelChoiceField(label='Holder', queryset=User.objects.all())
    ACCOUNT_BALANCE = forms.IntegerField(label='Balance', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Account
        fields = ('ACCOUNT_HOLDER', 'ACCOUNT_BALANCE')