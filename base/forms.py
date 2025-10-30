from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Event, Course

class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['EventDescription', 'Event_image']  
        
        labels = {
            'EventDescription': "",
        }
        
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['EventDescription'].widget.attrs.update({'class':'EventDescription'})
        self.fields['Event_image'].widget.attrs.update({'class':'Event_image'})

class createCourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ['host']
        fields = ['Course_name', 'Category','CourseDescription', 'video']  
        
        labels = {
            'Course_name' : "Enter Course Name"
        }
        
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Course_name'].widget.attrs.update({'class':'Coursename'})
        self.fields['Category'].widget.attrs.update({'class':'Coursename'})
        self.fields['CourseDescription'].widget.attrs.update({'class':'CourseDescription'})


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'inputs'})
        self.fields['email'].widget.attrs.update({'class':'inputs'})
        self.fields['password1'].widget.attrs.update({'class':'inputs'})
        self.fields['password2'].widget.attrs.update({'class':'inputs'})