from django import forms
from .models import Resume

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICE = [
    ('Mumbai','Mumbai'),
    ('pune','pune'),
    ('Hyderabad','Hyderabad'),
    ('Delhi','Delhi'),
]
class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    preferred_job_city = forms.MultipleChoiceField(choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','date_of_birth','gender','address','city','pin','state','mobile','email','preferred_job_city','myprofile','my_file']
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'pin' : forms.NumberInput(attrs={'class':'form-control'}),
            'state' : forms.Select(attrs={'class':'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            
               
        }