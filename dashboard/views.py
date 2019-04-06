from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .models import *

# Create your views here.
def bloglogin(request):
    if request.method == "GET":
        return render(request,'dashboard/login.html')
    elif request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return HttpResponseRedirect(reverse('login'))    
@login_required
def bloglogout(request):
    logout(request)
    context = {
        'message': 'Successfully logout'
    }
    return render(request,'dashboard/login.html',context)

@login_required
def create_category(request):
    if request.method== "GET":
        return render(request,"dashboard/create_category.html")

    if request.method =="POST":
        name = request.POST.get("cate_name",None)
        description = request.POST.get("cate_desc",None)
        data=Category.objects.create(category_name=name,category_description=description)
    return HttpResponseRedirect(reverse('allcategory'))

        
@login_required
def allcategory(request):
    all_category=Category.objects.all()
    return render(request,"dashboard/allcategory.html",{'all_category':all_category})


def postdelete(request,pk):
    Category.objects.filter(pk=pk).delete()
    messages.info(request,'Delete Post')
    return HttpResponseRedirect(reverse('allcategory'))

@login_required
def posts(request):
    if request.method== "GET":
        return render(request,"dashboard/posts.html")

    if request.method =="POST":
        title = request.POST.get("post_title",None)
        desc = request.POST.get("post_des",None)
        # print(title,desc)
        BlogPost.objects.create(title=title,details=desc)
    return HttpResponseRedirect(reverse('showallposts'))

def updatepost(request,pk):
    return render(request,"dashboard/posts.html")

def deletepost(request,pk):
    BlogPost.objects.filter(pk=pk).delete()
    messages.info(request,'Delete Post')
    return HttpResponseRedirect(reverse('showallposts'))
        
@login_required
def showallposts(request):
    all_post=BlogPost.objects.all()
    return render(request,"dashboard/showallpost.html",{'allpost':all_post})

@login_required
def updatepost(request,pk):

    if request.method== "GET":

        return render(request,"dashboard/updatepost.html")



@login_required
def settings(request):
    return render(request,"dashboard/settings.html")

@login_required
def dashboard(request):
    return render(request,"dashboard/home.html")