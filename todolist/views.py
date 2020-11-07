from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {}
    return render(request, 'todolist/index.html', context)

def signup(request):
    context = {}
    return render(request, 'todolist/signup.html', context)

