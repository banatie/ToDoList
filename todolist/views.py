from django.shortcuts import render
#from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    context = {}
    return render(request, 'todolist/index.html', context)

def signup(request):
    context = {}
    return render(request, 'todolist/signup.html', context)

def login(request):
    # Only Accept Post Request
    if request.method != 'POST':
        context = {'error_message' : 'Invalid HTTP request'}
        render(request, 'todolist/index.html', context)

    # Get email, password
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=email, password=password)
    if user is not None:
        context = {}
        return render(request, 'todolist/index.html', context)
    else:
        context = {'error_message' : 'Account not Found.'}
        return render(request, 'todolist/index.html', context)
