from django.shortcuts import render , redirect, HttpResponse
from .models import Category, Course, Event, Message, Chat
from .forms import  createEventForm, createCourseForm, SignUpForm
from django.template import loader
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def navbar(request):
    categories = Category.objects.all() 
    context = {'categories':categories}
    return render(request, 'navbar.html', context)


def videopage(request, pk):
    categories = Category.objects.all() 
    course = Course.objects.get(id=pk)
    messages = course.message_set.all()

    if request.method == 'POST' and request.POST.get('JOIN') == 'JOIN':
        course.participants.add(request.user)
        print('user joined')
    
    if request.method == 'POST' and request.POST.get('LEAVE') == 'LEAVE':
        course.participants.remove(request.user)
        print('user left')

    context = {'categories':categories, 'course':course, 'messages':messages}
    return render(request, 'videopage.html', context)

def comment(request,pk):
    course = Course.objects.get(id=pk)
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            course = course,
            body = request.POST.get('body') ##imported from room.html in input(named body)
        )
        print('hello')
        return redirect('videopage', pk=course.id)

    return render(request)

def events(request):
    categories = Category.objects.all() 
    events = Event.objects.all()
    context = {'categories':categories, 'events':events}
    return render(request, 'Events.html', context)

@login_required(login_url="login")
def postevent(request):
    form = createEventForm()
    events = Event.objects.all()
    if request.method == 'POST':
        form = createEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')
    
    categories = Category.objects.all() 
    context = {'categories':categories, 'form':form, 'events':events}
    
    return render(request, 'postevent.html', context)

@login_required(login_url="login")
def createpage(request):
    categories = Category.objects.all() 
    context = {'categories':categories}
    return render(request, 'createpage.html', context)


def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    courses = Course.objects.filter(
        Q(Category__Category_name__icontains=q) |
        Q(Course_name__icontains=q) 
    )
    categories = Category.objects.all() 
    # courses = Course.objects.all()  
    context = {
        'categories':categories, 
        'courses':courses,
        }
    return render(request, 'homepage.html', context)

@login_required(login_url="login")
def postcourse(request):
    categories = Category.objects.all() 
    form = createCourseForm()
    if request.method == 'POST':
        form = createCourseForm(request.POST, request.FILES)
        if form.is_valid():
            postform = form.save(commit = False)
            postform.host = request.user
            postform.save()
            return redirect('homepage')
    
    context = {'categories':categories, 'form':form}
    return render(request,'postcourse.html', context)


def loginpage(request):
    categories = Category.objects.all() 
    
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'this account does not exist')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,'password is incorrect')

    
    context = {'categories':categories, 'page':page}
    return render(request, 'loginpage.html', context)

def logoutpage(request):
    logout(request)
    return redirect('homepage')     

def signuppage(request):
    categories = Category.objects.all() 
    form = SignUpForm() 

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower() ## the user that was just created
            user.save()
            login(request, user) ## logs the user in after he was registerd in the database
            return redirect('homepage')
        else:
            messages.error(request,'An error occured during Registration')
    
    context = {'categories':categories, 'form':form}
    return render(request, 'signup.html', context)

def joinedcourses(request):
    categories = Category.objects.all() 
    courses = Course.objects.filter(participants = request.user)
    context = {'categories':categories,'courses':courses}
    return render(request, 'joinedcourses.html', context)


def editpage(request, pk):
    course = Course.objects.get(id=pk)
    form = createCourseForm(instance=course)
    
    if request.method == 'POST':
        form = createCourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form':form}
    return render(request, 'editpage.html',context)

def editevent(request, pk):
    event = Event.objects.get(id=pk)
    form = createEventForm(instance=event)
    
    if request.method == 'POST':
        form = createEventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form':form, 'event':event}
    return render(request, 'editpage.html',context)



@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id = pk)
    
    if request.user != message.user :
        return HttpResponse('Your are not allowed here!!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('homepage')

    return render(request,'deletepage.html')

@login_required(login_url='login')
def deleteevent(request,pk):
    event = Event.objects.get(id = pk)
    
    if request.method == 'POST':
        event.delete()
        return redirect('homepage')

    return render(request,'deletepage.html')


def deletecourse(request, pk):
    course =  Course.objects.get(id = pk)

    if request.method == 'POST':
        course.delete()
        return redirect('homepage')
   
    if request.user != course.host :
        return HttpResponse('You are not allowed here!!')


    return render(request,'deletepage.html')

def learnmore(request):
    return render(request,'learnmore.html')


@login_required(login_url='login')
def deleteChat(request, pk):
    message = Chat.objects.get(id = pk)
    
    if request.user != message.user :
        return HttpResponse('Your are not allowed here!!')
    
    if request.method == 'POST':
        message.delete()
        return redirect('Ask')
 
    return render(request,'deletepage.html')


def Ask(request):
    categories = Category.objects.all() 
    messages = Chat.objects.all()

    if request.method == 'POST':
        message = Chat.objects.create(
            user = request.user,
            body = request.POST.get('body') ##imported from room.html in input(named body)
        )
        return redirect('Ask')

    context = {'categories':categories, 'messages':messages}
    return render(request, 'Ask.html', context)



# def show_category(request, category_name):
#   template = loader.get_template('category.html')
#   context = {
#     'category': category_name,
#     # other variables
#   }
# #   return HttpResponse(template.render(context, request))

# {% if category == 'maths' %}
#   <img src="maths_image.jpg" alt="Maths image">
# {% endif %}