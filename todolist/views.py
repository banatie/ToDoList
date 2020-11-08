from django.shortcuts import render
#from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {}
    return render(request, 'todolist/index.html', context)

def signup(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'todolist/index.html', context)
    
    if request.method == 'GET':
        context = {}
        return render(request, 'todolist/signup.html', context)
    elif request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
        except KeyError:
            context = {'error_message' : 'Email or Password is not Found'}
            return render(request, 'todolist/signup.html', context)
        user = User.objects.create_user(username=email, password=password)
        auth_login(request, user)
        context = {}
        return render(request, 'todolist/index.html', context)
        """
        if user is not None:
            login(request, user)
            context = {}
            return render(request, 'todolist/index.html', context)
        else:
            context = {'error_message' : 'Authentication Failed'}
            return render(request, 'todolist/signup.html', context)
        """

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
        login(request, user)
        context = {}
        return render(request, 'todolist/index.html', context)
    else:
        context = {'error_message' : 'Account not Found.'}
        return render(request, 'todolist/index.html', context)

def user_logout(request):
    logout(request)
    context = {}
    return render(request, 'todolist/index.html', context)
