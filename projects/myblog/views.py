from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.


def index(request):
    return render(request, 'index.html')


def counter(request):
    return render(request, 'words.html')


def handleCounter(request):
    words = request.POST['words']
    counter = len(words.split())
    return render(request, 'handleCounter.html', {'words': counter})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def handleRegister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('handleRegister')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('handleRegister')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('handleRegister')
    else:
        return render(request, 'handleRegister.html')
