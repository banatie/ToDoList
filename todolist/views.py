from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'todolist/index.html', context)
    
def signup(request):
    return HttpResponse('signup!!!')
