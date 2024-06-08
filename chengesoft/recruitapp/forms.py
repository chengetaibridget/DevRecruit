from . models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput,IntegerField
class UserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control",'placeholder': 'Password','required': 'required'})
        self.fields["password2"].widget.attrs.update({"class": "form-control",'placeholder': 'Confirm Password','required': 'required'})
    class Meta:
        model = User
        fields = ['firstname','lastname' ,'username','dob','phone','email','address','education','institute','password1', 'password2']

        widgets = {
            'firstname' : forms.TextInput(attrs = {'class':'form-control','placeholder': 'firstname'}),
            'lastname' : forms.TextInput(attrs = {'class':'form-control','placeholder': 'lastname'}),
            'username' : forms.TextInput(attrs = {'id':'usernamefield','class':'form-control','placeholder':'username'}),
            'phone' : forms.TextInput(attrs = {'class':'form-control','placeholder':'phone'}),
            'email' : forms.EmailInput(attrs = {'id':'emailfield','class':'form-control','placeholder':'email'}),
            'address' : forms.TextInput(attrs = {'class':'form-control','placeholder':'address'}), 
            'dob' : forms.DateTimeInput(attrs = {'class':'form-control','placeholder':'date of birth'}), 
            'education' : forms.TextInput(attrs = {'class':'form-control','placeholder':'education'}),
            'institute' : forms.TextInput(attrs = {'class':'form-control','placeholder':'institute'}),
           
               
        }


class PracticalForm(forms.ModelForm):
    class Meta:
        model=Practical
        fields=['test_number','test_title','test_name','test_details','expected_result','mark']
        widgets = {
            'test_number':forms.TextInput(attrs = {'class':'form-control','placeholder': 'test number'}),
            'test_title':forms.TextInput(attrs = {'class':'form-control','placeholder': 'test title'}),
            'test_name':forms.TextInput(attrs = {'class':'form-control','placeholder': 'test name'}),
            'test_details' : forms.Textarea(attrs = {'class':'form-control','placeholder':'details','id':'summernote'}),
            'expected_result':forms.TextInput(attrs = {'class':'form-control','placeholder': 'Expected Result'}),
            'mark' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Mark'}),
        }


class TheoryForm(forms.ModelForm):
    class Meta:
        model=Theorytest
        fields=['question','option1','option2','option3','option4','answer']
        widgets = {
            'question':forms.Textarea(attrs = {'class':'form-control','placeholder': 'Question'}),
            'option1':forms.TextInput(attrs = {'class':'form-control','placeholder': 'option 2'}),
            'option2':forms.TextInput(attrs = {'class':'form-control','placeholder': 'option 2'}),
            'option3':forms.TextInput(attrs = {'class':'form-control','placeholder': 'option 3'}),
            'option4':forms.TextInput(attrs = {'class':'form-control','placeholder': 'option 4'}),
            'answer':forms.TextInput(attrs = {'class':'form-control','placeholder': 'answer'}),
           
           
        }

        