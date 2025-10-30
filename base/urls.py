from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('navbar/', views.navbar),
    path('videopage/<str:pk>/', views.videopage, name="videopage"),
    path('comment/<str:pk>/', views.comment, name="comment"),
    path('events/', views.events, name="events"),
    path('postevent/', views.postevent, name="postevent"),
    path('createpage/', views.createpage, name="createpage"),
    path('postcourse/', views.postcourse, name="postcourse"),
    path('login/', views.loginpage, name= "login"),
    path('logout/', views.logoutpage, name='logout'),
    path('signup/', views.signuppage, name='signup'),
    path('joinedcourses/', views.joinedcourses, name='joinedcourses'),
    path('editpage/<str:pk>', views.editpage, name='editpage'),
    path('deletepage/<str:pk>', views.deletecourse, name='deletepage'),
    path('deleteMessage/<str:pk>', views.deleteMessage, name='deleteMessage'),
    path('editevent/<str:pk>', views.editevent, name='editevent'),
    path('deleteevent/<str:pk>', views.deleteevent, name='deleteevent'),
    path('learnmore/', views.learnmore, name='learnmore'),
    path('Ask/', views.Ask, name='Ask'),
    path('Ask/', views.Ask, name='Ask'),
    path('deleteChat/<str:pk>', views.deleteChat, name="deleteChat"),
]