from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question,Answer,Blog
from datetime import datetime
from django.core import serializers
from django.shortcuts import redirect,get_object_or_404 
from django.urls import reverse
from .forms import BlogForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        question1=request.POST['ques']
        p = Question(ques=question1 , pub_date = datetime.now())
        p.save()
    context = {
        "question":Question.objects.all()
    }   
    return render(request,'second.html',context)

def ask_question(request):
    return render(request, "ask.html",{})

def view_question(request,id=None):

    post=get_object_or_404(Question,id=id)

    if request.method=="POST":
        answer=request.POST['answer']
        a=Answer(ques=post,ans=answer,pub_date=datetime.now())
        a.save()

    context={
        "answers":Answer.objects.filter(ques=post),
        "question":post
    }

    return render(request, 'viewquestion.html', context)

def blog(request):
    form=BlogForm(request.POST or None)
    
    if form.is_valid():
        form.save()
    
    context={'form':form,'blog':Blog.objects.all()}
    return render(request,'blog.html',context)

def visitblog(request,id=None):

    vb=get_object_or_404(Blog,id=id)
    context={
        'blog':vb
    }
    return render(request,'visitblog.html',context)