from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),

    path('index.html', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),

    path('game.html', views.game, name="game"),
    path('blogpost.html', views.blogpost, name="blogpost"),
    path('blogpost1.html', views.blogpost1, name="blogpost1"),
    path('blogpost3.html', views.blogpost3, name="blogpost3"),
    path('blogpost4.html', views.blogpost4, name="blogpost4"),

]
