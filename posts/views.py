from django.shortcuts import render



def index(request):
    return render(request, 'index.html', {})

def music(request):
    return render(request, 'music.html', {})

def contatti(request):
    return render(request, 'contatti.html', {})

def guitar(request):
    return render(request, 'guitar.html', {})

def news(request):
    return render(request, 'news.html', {})

def login(request):
    return render(request, 'login.html', {})


# Create your views here.
