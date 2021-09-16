from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('changepassword/', views.change_password, name='changepassword'),
    path('Login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('movies/', views.movieview, name='movies'),
    path('Create', views.minsert, name='minsert'),
    path('CreateRatings', views.rinsert, name='rinsert'),
    path('CreateLinks', views.linsert, name='linsert'),
    path('CreateTags', views.tinsert, name='tinsert'),

    path('tags/', views.tagview, name='tags'),
    path('ratings/', views.ratingview, name='ratings'),
    path('links/', views.linkview, name='links'),
]
