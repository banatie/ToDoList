from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from todolist.models import Todo


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
        try:
            user = User.objects.get(username=email)
            context = {'error_message' : 'The Email is already taken'}
            return render(request, 'todolist/signup.html', context)
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, email=email, password=password)
        login(request, user)
        context = {}
        return render(request, 'todolist/index.html', context)
 
def user_login(request):
    # Only Accept Post Request
    if request.method != 'POST':
        context = {'error_message' : 'Invalid HTTP request'}
        render(request, 'todolist/index.html', context)

    try:
        # Get email and password
        email = request.POST['email']
        password = request.POST['password']
    except KeyError:
        context = {'error_message' : 'Email or Password is not Found'}
        return render(request, 'todolist/index.html', context)

    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('todolist:index'))
    else:
        context = {'error_message' : 'Account not Found.'}
        return render(request, 'todolist/index.html', context)

def user_logout(request):
    logout(request)
    context = {}
    return render(request, 'todolist/index.html', context)
