from django import forms

from Dell.models import Login, registrationForm
#from Dell.models import loginForm
#from Dell.models import registrationForm

'''class LoginForm(forms.ModelForm):
    Username = forms.EmailField(max_length=63,required=True)
    Password1 = forms.CharField(max_length=83 , widget=forms.PasswordInput,required=True)
    
    class Meta:
        model = Login
        fields = ['Username', 'Password1',]
        labels = { 'Username':"Email", 'Password1':"Password"}
        
class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=80)
    mob = forms.IntegerField()
    first_Name = forms.CharField(max_length=255)
    last_Name = forms.CharField(max_length=255)
    
    class Meta:
        model = U
        fields = ('username', 'password1', 'password2' ,'email', )
        labels = {'mob': 'Mobile Number','first':'First Name','last':'Last Name',}'''
        
'''class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=455,required=True)
    email = forms.EmailField(max_length=643,required=True,widget=forms.TextInput())
    password1 = forms.CharField(max_length=83, widget=forms.PasswordInput,required=True)
    Password = forms.CharField(max_length=83,widget=forms.PasswordInput,required=True)
    class Meta:
        model = registrationForm
        fields = ['email', 'password1','Password','name',]'''
''' Middle_Name = forms.CharField(max_length=445)
    Last_Name = forms.CharField(max_length=345)
    Mob = forms.IntegerField(max_length=14)
    Address = forms.CharField(max_length=877)
    Gender = forms.ModelFormOptions(Male='male',Female='female',other='other')'''
    
    