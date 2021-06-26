from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
 
# Tworzymy nowe widoki
def home(request):
    if request.method=="POST":
        return redirect('home')
    else:
        context={}
        return render(request, 'Quiz/home.html', context)

def maths(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Matematyka.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.mat))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.mat):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=Matematyka.objects.all()
        context = {
            'mats':questions
        }
        return render(request,'Quiz/maths.html',context)

def physics(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Fizyka.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.fiz))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.fiz):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=Fizyka.objects.all()
        context = {
            'fizs':questions
        }
        return render(request,'Quiz/physics.html',context)
 
def history(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Historia.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.his))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.his):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=Historia.objects.all()
        context = {
            'hiss':questions
        }
        return render(request,'Quiz/history.html',context)

def informatics(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Informatyka.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.inf))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.inf):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=Informatyka.objects.all()
        context = {
            'infs':questions
        }
        return render(request,'Quiz/informatics.html',context)
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')
