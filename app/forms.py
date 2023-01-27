from django import forms  
from .models import  companysetup,Login, employee 


class LoginForm(forms.ModelForm):  
    class Meta:  
        model = Login  
        fields = "__all__" 


class companySetupForm(forms.ModelForm):  
    class Meta:  
        model = companysetup  
        fields = "__all__" 


class employeeForm(forms.ModelForm):  
    class Meta:  
        model = employee  
        fields = "__all__" 