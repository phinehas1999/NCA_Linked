from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    Category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.Category_name

class Course(models.Model):
    Course_name = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    participants = models.ManyToManyField(User, related_name='participants',blank=True)
    CourseDescription = models.TextField(null=True)

    video = models.FileField(upload_to="videos/", null=True, blank=True)

    def __str__(self):
        return self.Course_name

    # self.CourseDescription

    class Meta():
        ordering = ['-updated','-created']

        
class Event(models.Model):
    EventDescription = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    Event_image = models.ImageField(null=True, blank=True, upload_to="images/") 
    class Meta():
        ordering = ['-created']

    def __str__(self):
        return self.EventDescription


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True) 
    
    class Meta():
        ordering = ['-created', '-updated']  

    def __str__(self):
        return self.body[0:50] 
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True) 
    
    class Meta():
        ordering = ['-created', '-updated']  

    def __str__(self):
        return self.body[0:50] 
    
