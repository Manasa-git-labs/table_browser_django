from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth import login
from django.contrib import messages
def home(request):
 return render(request, 'app/home.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def login(request):
    return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def movieview(request):

     table = movies.objects.all()
     return render(request, 'app/movies.html', {'data': table})

def minsert(request):
    if request.method=="POST":
        if request.POST.get('movieid') and request.POST.get('title') and request.POST.get('geners'):

            saver=movies()
            saver.movieid=request.POST.get('movieid')
            saver.title = request.POST.get('title')
            saver.geners = request.POST.get('geners')
            saver.save()
            messages.success(request,"record added!!!!!"+saver.title+"in database now")
            return render(request,"app/Create.html")
    else:
            return render(request, "app/Create.html")

def tagview(request):
    table = tags.objects.all()
    return render(request, 'app/tags.html', {'data' : table})

def tinsert(request):
    if request.method=="POST":
        if request.POST.get('userid') and request.POST.get('titleid') and request.POST.get('tag') and request.POST.get('timestamp'):

            saver=tags()
            saver.userid = request.POST.get('userid')
            saver.titleid=request.POST.get('titleid')
            saver.tag = request.POST.get('tag')
            saver.timestamp = request.POST.get('timestamp')
            saver.save()
            messages.success(request,"record added!!!!!"+saver.title+"in database now")
            return render(request,"app/CreateTags.html")
    else:
            return render(request, "app/CreateTags.html")



def ratingview(request):
    table = ratings.objects.all()
    return render(request, 'app/ratings.html', {'data' : table})

def rinsert(request):
    if request.method=="POST":
        if request.POST.get('userid') and request.POST.get('titleid') and request.POST.get('rating') and request.POST.get('timestamp'):

            saver=ratings()
            saver.userid=request.POST.get('userid')
            saver.titleid = request.POST.get('titleid')
            saver.rating = request.POST.get('rating')
            saver.timestamp = request.POST.get('timestamp')
            saver.save()
            messages.success(request,"record added!!!!!"+saver.titleid+"in database now")
            return render(request,"app/CreateRatings.html")
    else:
            return render(request, "app/CreateRatings.html")

def linkview(request):
    table = links.objects.all()
    return render(request, 'app/links.html', {'data' : table})


def linsert(request):
    if request.method=="POST":
        if request.POST.get('movieid') and request.POST.get('imdbid') and request.POST.get('tmdbid'):

            saver=links()
            saver.movieid=request.POST.get('movieid')
            saver.imdbid = request.POST.get('imdbid')
            saver.tmdbid = request.POST.get('tmdbid')
            saver.save()
            messages.success(request,"record added!!!!!"+saver.movieid+"in database now")
            return render(request,"app/CreateLinks.html")
    else:
            return render(request, "app/CreateLinks.html")

