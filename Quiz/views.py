from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpRequest
from .forms import *


def search_categories(request: HttpRequest) -> HttpResponse:
    categories: list[Category] = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'Quiz/categories.html', context)


def search_quizzes(request: HttpRequest, category_id: int) -> HttpResponse:
    quizzes: list[Quizz] = Quizz.objects.filter(category=category_id)
    
    context = {
        'quizzes': quizzes
    }

    return render(request, 'Quiz/quizzes.html', context)


def get_quizz(request: HttpRequest, quizz_id: int) -> HttpResponse:
    quizz: Quizz = Quizz.objects.get(id=quizz_id)

    context = {
        'quizz_id': quizz.id,
        'questions': quizz.questions
    }

    return render(request, 'Quiz/quizz.html', context)


def get_results(request: HttpRequest, quizz_id: int) -> HttpResponse:
    if request.method != "POST":
        return redirect('categories')
    
    questions: list[Question] = Quizz.objects.get(id=quizz_id).questions
    score: int = 0
    wrong: int = 0
    correct: int = 0
    total: int = questions.count()
    for q in questions.all():
        for a in q.answers.all():
            if str(a.id) == request.POST.get(str(q.id)):
                if (a.correct):
                    score += 10
                    correct += 1
                else:
                    wrong += 1

    percent: float = score/(total*10) * 100
    context = {
        'score': score,
        'time': request.POST.get('timer'),
        'correct': correct,
        'wrong': wrong,
        'percent': percent,
        'total': total
    }

    return render(request,'Quiz/result.html',context)


def home(request: HttpRequest) -> HttpResponse:
    if request.method=="POST":
        return redirect('categories')
    else:
        context={}
        return redirect('categories')

 
def registerPage(request: HttpRequest) -> HttpResponse:
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
 

def loginPage(request: HttpRequest) -> HttpResponse:
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
 

def logoutPage(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('/')
